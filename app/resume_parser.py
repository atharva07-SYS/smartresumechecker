nltk.download('punkt')
nltk.download('stopwords')

import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def extract_skills(text):
    stop_words = set(stopwords.words('english'))
    # Define categories
    coding_languages = [
        # 💻 Technical Skills
        'python', 'java', 'c++', 'visual basic', 'cobol', 'sql', 'html', 'unix', 'linux', 'windows systems',
        'web-based networking', 'programming', 'computerized accounting systems', 'software development',
        'systems design', 'database management', 'information systems', 'microcomputer graphics',
        'ms office', 'word', 'excel', 'powerpoint', 'access', 'outlook', 'internet applications',
        'relational databases', 'technical support', 'troubleshooting', 'networking', 'operating systems',
        'data entry', 'ms project', 'spss', 'quickbooks',
        # Other programming languages and tools
        'c', 'c#', 'javascript', 'typescript', 'css', 'php', 'asp', 'perl', 'matlab', 'r', 'scala', 'go', 'golang',
        'ruby', 'swift', 'kotlin', 'objective-c', 'bash', 'shell', 'powershell', 'assembly', 'fortran', 'vhdl',
        'verilog', 'julia', 'stata', 'pl/sql', 'abap', 'groovy', 'dart', 'lua', 'rust', 'haskell', 'prolog', 'lisp',
        'clojure', 'f#', 'delphi', 'pascal', 'erlang', 'elm', 'ocaml', 'racket', 'scheme', 'smalltalk', 'ada', 'awk',
        'scratch', 'labview', 'mysql', 'postgresql', 'mongodb', 'firebase', 'oracle', 'graphql', 'json', 'xml', 'jsx', 'tsx'
    ]
    spoken_languages = [
        'english', 'hindi', 'marathi', 'gujarati', 'punjabi', 'bengali', 'tamil', 'telugu', 'kannada', 'malayalam',
        'urdu', 'oriya', 'assamese', 'maithili', 'santali', 'kashmiri', 'dogri', 'konkani', 'manipuri', 'bodo',
        'sanskrit', 'french', 'german', 'spanish', 'portuguese', 'russian', 'arabic', 'japanese', 'korean', 'chinese',
        'thai', 'vietnamese', 'burmese', 'khmer', 'lao', 'mongolian', 'nepali', 'sinhala', 'greek', 'italian', 'turkish',
        'polish', 'dutch', 'swedish', 'norwegian', 'danish', 'finnish', 'hebrew', 'croatian', 'serbian', 'slovak',
        'slovenian', 'romanian', 'bulgarian', 'czech', 'hungarian'
    ]
    app_tools = [
        # MS Office and productivity
        'ms office', 'word', 'excel', 'powerpoint', 'access', 'outlook', 'onenote', 'visio', 'microsoft office',
        'ms project', 'google docs', 'google sheets', 'google slides', 'google drive', 'dropbox', 'slack', 'zoom',
        'teams', 'skype', 'webex', 'jira', 'confluence', 'notion', 'trello', 'asana', 'evernote',
        # Development and analytics
        'github', 'gitlab', 'bitbucket', 'docker', 'kubernetes', 'jenkins', 'travis', 'circleci', 'firebase', 'aws',
        'azure', 'gcp', 'vmware', 'virtualbox', 'hyper-v', 'ansible', 'chef', 'puppet', 'selenium', 'appium', 'junit',
        'pytest', 'unittest', 'mocha', 'chai', 'jest', 'enzyme', 'cypress', 'robot framework', 'tableau', 'powerbi',
        'spss', 'sas', 'matlab', 'stata', 'r', 'pandas', 'numpy', 'scikit-learn', 'tensorflow', 'keras', 'pytorch',
        'hadoop', 'spark', 'mysql', 'postgresql', 'oracle', 'mongodb', 'nosql', 'rest', 'api', 'graphql', 'json', 'xml',
        # IDEs and editors
        'android', 'ios', 'xcode', 'android studio', 'visual studio', 'eclipse', 'intellij', 'pycharm', 'sublime',
        'vscode', 'notepad++', 'vim', 'emacs',
        # Accounting and business
        'quickbooks',
    ]
    hobbies = [
        'reading', 'writing', 'traveling', 'cooking', 'dancing', 'singing', 'painting', 'drawing', 'photography',
        'blogging', 'gaming', 'sports', 'football', 'cricket', 'basketball', 'badminton', 'tennis', 'swimming',
        'cycling', 'hiking', 'trekking', 'yoga', 'meditation', 'gardening', 'music', 'movies', 'volunteering',
        'acting', 'sketching', 'chess', 'puzzles', 'board games', 'crafts', 'poetry', 'calligraphy', 'fishing',
        'bird watching', 'collecting', 'baking', 'martial arts', 'surfing', 'skating', 'skiing', 'snowboarding',
        'mountaineering', 'scuba diving', 'paragliding', 'adventure sports', 'robotics', 'astronomy', 'astrophotography'
    ]
    # Lowercase sets for fast lookup
    coding_set = set(coding_languages)
    spoken_set = set(spoken_languages)
    app_set = set(app_tools)
    hobby_set = set(hobbies)

    # Split into lines and normalize
    lines = text.lower().split('\n')
    phone_pattern = re.compile(r'\(?\d{3}\)?[-\s.]?\d{3}[-\s.]?\d{4}')
    symbol_pattern = re.compile(r'[•]')

    found_coding = set()
    found_spoken = set()
    found_apps = set()
    found_hobbies = set()

    for line in lines:
        line = symbol_pattern.sub('', line)
        line = phone_pattern.sub('', line)
        line = re.sub(r'[^\w\s+]', '', line)
        line = re.sub(r'\s+', ' ', line).strip()
        if len(line) < 2:
            continue
        words = word_tokenize(line)
        filtered_words = [w for w in words if w not in stop_words and len(w) > 1]
        final_line = ' '.join(filtered_words)
        # Check for coding languages
        for skill in coding_set:
            if skill in final_line:
                found_coding.add(skill.title())
        # Check for spoken languages
        for lang in spoken_set:
            if lang in final_line:
                found_spoken.add(lang.title())
        # Check for app/tools
        for app in app_set:
            if app in final_line:
                found_apps.add(app.title())
        # Check for hobbies
        for hobby in hobby_set:
            if hobby in final_line:
                found_hobbies.add(hobby.title())

    return {
        'Technical Skills': sorted(found_coding),
        'Spoken Languages': sorted(found_spoken),
        'Applications/Tools': sorted(found_apps),
        'Hobbies': sorted(found_hobbies)
    }

def clean_and_format_skills(raw_text):
    stop_words = set(stopwords.words('english'))
    # List of technical/coding skills to focus on
    coding_keywords = [
        'python', 'java', 'c', 'c++', 'c#', 'javascript', 'typescript', 'html', 'css', 'sql', 'php', 'asp', 'perl',
        'unix', 'linux', 'windows', 'bash', 'shell', 'powershell', 'matlab', 'r', 'tableau', 'sas', 'spss',
        'machine learning', 'deep learning', 'tensorflow', 'pytorch', 'keras', 'scikit-learn', 'pandas', 'numpy',
        'data analysis', 'data science', 'big data', 'hadoop', 'spark', 'aws', 'azure', 'gcp', 'cloud',
        'docker', 'kubernetes', 'devops', 'git', 'github', 'bitbucket', 'gitlab', 'visual basic', 'cobol',
        'microcomputer applications', 'database', 'sql server', 'mysql', 'postgresql', 'nosql', 'mongodb',
        'firebase', 'oracle', 'pl/sql', 'rest', 'api', 'graphql', 'json', 'xml', 'android', 'ios', 'swift',
        'objective-c', 'react', 'angular', 'vue', 'node', 'nodejs', 'express', 'django', 'flask', 'fastapi',
        'spring', 'dotnet', '.net', 'ruby', 'rails', 'go', 'golang', 'scala', 'rust', 'assembly', 'verilog',
        'vhdl', 'embedded', 'arm', 'fpga', 'vlsi', 'mathematica', 'stata', 'julia', 'sas', 'powershell',
        'networking', 'tcp/ip', 'udp', 'http', 'https', 'ssl', 'tls', 'encryption', 'cybersecurity',
        'penetration testing', 'ethical hacking', 'reverse engineering', 'malware analysis', 'wireshark',
        'virtualization', 'vmware', 'hyper-v', 'virtualbox', 'ansible', 'chef', 'puppet', 'jenkins',
        'travis', 'circleci', 'ci/cd', 'testing', 'unit testing', 'integration testing', 'selenium',
        'appium', 'junit', 'pytest', 'unittest', 'mocha', 'chai', 'jest', 'enzyme', 'cypress',
        'robot framework', 'jira', 'confluence', 'notion', 'trello', 'asana', 'microsoft office',
        'ms office', 'ms word', 'ms excel', 'ms powerpoint', 'ms outlook', 'ms access', 'ms project',
        'ms visio', 'google docs', 'google sheets', 'google slides', 'google drive', 'dropbox',
        'slack', 'zoom', 'teams', 'skype', 'webex', 'trello', 'asana', 'notion', 'evernote', 'onenote',
        'outlook', 'email', 'calendar', 'scheduling', 'travel planning', 'expense reporting',
        'presentation skills', 'public speaking', 'writing', 'editing', 'proofreading', 'copywriting',
        'content writing', 'blogging', 'seo', 'sem', 'social media', 'facebook', 'twitter', 'linkedin',
        'instagram', 'youtube', 'video editing', 'photography', 'illustration', 'animation',
        'customer engagement', 'customer retention', 'upselling', 'cross-selling', 'cold calling',
        'lead generation', 'market research', 'competitive analysis', 'product management',
        'product development', 'product marketing', 'go-to-market', 'launch', 'pricing', 'branding',
        'advertising', 'media buying', 'media planning', 'event marketing', 'trade shows',
        'conferences', 'webinars', 'email marketing', 'direct mail', 'print production',
        'copy editing', 'proofreading', 'translation', 'multilingual', 'bilingual', 'spanish',
        'french', 'german', 'chinese', 'japanese', 'korean', 'portuguese', 'russian', 'arabic',
        'hindi', 'bengali', 'urdu', 'italian', 'turkish', 'polish', 'dutch', 'swedish', 'norwegian',
        'danish', 'finnish', 'greek', 'czech', 'hungarian', 'romanian', 'bulgarian', 'croatian',
        'serbian', 'slovak', 'slovenian', 'hebrew', 'thai', 'vietnamese', 'indonesian', 'malay',
        'filipino', 'tagalog', 'burmese', 'khmer', 'lao', 'mongolian', 'nepali', 'sinhala', 'tamil',
        'telugu', 'kannada', 'malayalam', 'marathi', 'punjabi', 'gujarati', 'oriya', 'assamese',
        'maithili', 'santali', 'kashmiri', 'dogri', 'konkani', 'manipuri', 'bodo', 'sanskrit', 'english'
    ]
    coding_keywords = set([k.lower() for k in coding_keywords])

    # Split into lines and normalize
    lines = raw_text.lower().split('\n')
    cleaned_lines = set()

    # Pattern for phone numbers and unnecessary symbols
    phone_pattern = re.compile(r'\(?\d{3}\)?[-\s.]?\d{3}[-\s.]?\d{4}')
    symbol_pattern = re.compile(r'[•]')

    for line in lines:
        line = symbol_pattern.sub('', line)
        line = phone_pattern.sub('', line)
        line = re.sub(r'[^\w\s+]', '', line)
        line = re.sub(r'\s+', ' ', line).strip()
        if len(line) < 2:
            continue
        # Remove stopwords from individual words in line
        words = word_tokenize(line)
        filtered_words = [w for w in words if w not in stop_words and len(w) > 1]
        final_line = ' '.join(filtered_words)
        # Only keep lines that match coding/technical keywords
        for skill in coding_keywords:
            if skill in final_line:
                cleaned_lines.add(skill.title())
    return sorted(cleaned_lines)

def extract_resume_text(path):
    """Extracts text from TXT, PDF, or DOCX files."""
    import os
    ext = os.path.splitext(path)[1].lower()
    if ext == '.pdf':
        import pdfplumber
        text = ''
        try:
            with pdfplumber.open(path) as pdf:
                for page in pdf.pages:
                    text += page.extract_text() or ''
        except Exception as e:
            # Log the error and return a user-friendly message
            print(f"PDF extraction error: {e}")
            return "[Error: Could not extract text from PDF. The file may be corrupted or invalid.]"
        return text
    elif ext == '.docx':
        from docx import Document
        doc = Document(path)
        return '\n'.join([para.text for para in doc.paragraphs])
    else:
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            return f.read()
