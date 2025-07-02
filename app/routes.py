
import os
import json
from flask import Blueprint, render_template, request, send_from_directory
from .resume_parser import extract_resume_text, extract_skills
from .jd_samples import JD_SAMPLES

main = Blueprint('main', __name__)

@main.route('/admin')
def admin_dashboard():
    logs = []
    uploads_dir = 'uploads'
    if os.path.exists(uploads_dir):
        for fname in os.listdir(uploads_dir):
            if fname.startswith('match_') and fname.endswith('.json'):
                try:
                    with open(os.path.join(uploads_dir, fname), 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        data['log_file'] = fname
                        logs.append(data)
                except Exception:
                    pass
    logs.sort(key=lambda x: x.get('timestamp', ''), reverse=True)
    return render_template('admin_dashboard.html', logs=logs)

@main.route('/uploads/<path:filename>')
def uploaded_file(filename):
    return send_from_directory('uploads', filename, as_attachment=True)

@main.route('/')
def index():
    return render_template('index.html')

# New route for resume + JD matching

@main.route('/match', methods=['POST'])
def match():
    file = request.files.get('resume')
    jobdesc = request.form.get('jobdesc', '')
    suggestions = []
    if file and jobdesc:
        path = os.path.join('uploads', file.filename)
        file.save(path)
        resume_text = extract_resume_text(path)
        jd_text = jobdesc

        resume_skills = extract_skills(resume_text)
        jd_skills = extract_skills(jd_text)

        # Only match technical skills
        resume_tech = set(resume_skills['Technical Skills'])
        jd_tech = set(jd_skills['Technical Skills'])
        matched = sorted(resume_tech & jd_tech)
        match_score = int((len(matched) / len(jd_tech) * 100) if jd_tech else 0)

        # JD Suggestions
        def jd_similarity(jd_skills, user_skills):
            return len(set(jd_skills).intersection(user_skills))
        if resume_skills['Technical Skills']:
            for jd in JD_SAMPLES:
                sim = jd_similarity([s.lower() for s in jd['skills']], [s.lower() for s in resume_skills['Technical Skills']])
                if sim > 0:
                    suggestions.append((sim, jd))
            suggestions.sort(reverse=True, key=lambda x: x[0])
            suggestions = [jd for sim, jd in suggestions[:3]]  # Top 3

        # Save log as JSON
        import json
        import datetime
        log_data = {
            'timestamp': datetime.datetime.now().isoformat(),
            'resume_filename': file.filename,
            'resume_skills': resume_skills,
            'jd_skills': jd_skills,
            'matched_skills': matched,
            'match_score': match_score
        }
        log_path = os.path.join('uploads', f"match_{file.filename}_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.json")
        with open(log_path, 'w', encoding='utf-8') as f:
            json.dump(log_data, f, indent=2)

        # Downloadable TXT report
        report_txt = f"Matched Skills:\n- {'\n- '.join(matched)}\n\nMatch Score: {match_score}%\n"
        report_filename = f"match_report_{file.filename}.txt"
        with open(os.path.join('uploads', report_filename), 'w', encoding='utf-8') as f:
            f.write(report_txt)

        # Render advanced result page
        return render_template(
            "result.html",
            match_score=match_score,
            matched=matched,
            report_filename=report_filename,
            resume_skills=resume_skills,
            jd_skills=jd_skills,
            jd_suggestions=suggestions
        )
    return "Upload or job description missing."
