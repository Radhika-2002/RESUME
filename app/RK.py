from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def resume():
    name = "Radhika Katiyara"
    title = "Software Developer"
    about = "Software Engineer with an understanding of delivering high-quality software products on time and within budget and proficient in Java, Python, and JavaScript with expertise in machine learning. Unveiling insights from data."
    email = "radhika.katiyara@gmail.com"
    contact_number = "(+91)8655256117"
    LinkedIn = "https://www.linkedin.com/in/radhika-katiyara-7a958b1ab/"
    Github = "Radhika-2002"


    education = [
        {
            "school": "Smt.V.D.Gardi High School",
            "degree": "Secondary High School",
            "year": "June 2016-June 2017"
        },
	{
            "college": "SK Somaiya Vinay Madir Jr.College",
            "degree": "High Secondary,Science",
            "year": "June 2017-June 2019"
        },
	{
            "college": "Vivekanand Education Society’s Institute of Technology",
            "degree": "B.Tech, Computer Science",
            "year": "Aug 2019- May 2023"
        }
    ]
    academic_projects = [
   	{
		"project_name": "Placement Record System",
		"duration": "Aug 2019-May 2021",          	                                                                         
		"description": [
            "Analyzed and surveyed the placement process, with the team, to ensure proper management of placement records.",
            "Technologies used for building are HTML, CSS, Firebase and PHP.",
            "Downloadable reports in form of pdf.",
	    "Generates Overall Placement summary and easy search function."
        ]
	},
	{
		"project_name": "Patient Treatment Recommendation Model",
		"duration": "Aug 2021-May 2022" ,         	                                                                         
		"description": [
		"Analyzed and surveyed problem statement, with the team to advance in health technology.",
		"Technologies used for building are HTML, CSS, Python, Flask.",
		"Predicts disease according to symptoms entered and then recommends first-aid and medications to the patient.",
		"Presented and published name Title :MedEstimate: Patient Treatment Recommendation model at IEEE Xplore Digital Library (ICAST-2022).https://ieeexplore.ieee.org/document/10039522"
	]
	},
	{
		"project_name": "AI-Based Water Quality Index (WQI) Analysis of Maharashtra", 
		"duration": "Aug 2022-June 2023",         	                                                                         
		"description": [
		"Analyzed and surveyed problem statement, with the team to propose a better solution for improving WQI of Maharashtra.",
		"Proposed a portable 5G module sensor which will be useful for measuring WQI easily.",
		"Technologies used for building ML models were Python and its libraries.",
		"Received acceptance for paper International Conference on Innovative Research in Science and Technology (IRST-2023) and selected for publication in Springer Nature.",
		"Received acceptance for paper 3rd ( Proceedings by Springer and Technically associated with ACM and Namibia University of Science and Technology)  IDBA-ACMWIR-2023 and selected for publication in conference proceedings by Springer. Electronic ISSN: 2731-5568 Print ISSN: 2731-555X, Series: “Data-Intensive Research”"
	]
	}
    ]
    internships = [
        {
            "title": "Web development internship",
            "company": "The Sparks Foundation",
            "duration": "April 2021",
            "description": "In this internship I was given the task to develop a website on Payment Gateway Integration. I built this website using the following languages and technologies :HTML, CSS, razorpay. Also it was hosted on Heroku. Link: https://paymentt.herokuapp.com/"
        },
        {
            "title": "Web development internship",
            "company": "VESIT Renaissance",
            "duration": "June 2021-July 2021",
            "description": "In this internship my team was given a task to develop a website on a green credit management system. We built this website using following languages and technologies : HTML, CSS, PHP, SQL,Python"
        },
	{
            "title": "Web development internship",
            "company": "LetsGrowMore",
            "duration": "Aug 2021-Sep 2021",
            "description": "In this internship I was given 2 tasks. The first was to develop a single page website and second was to generate API’s of users using ReactJS.I built this website using following languages and technologies : HTML, CSS, ReactJS."
        }
    ]
    experience = [
        {
            "title": "Designer and editor",
            "company": "Newsletter team at VESIT, Mumbai",
            "duration": "April 2021-May 2023",
            "description": "Designing and editing newsletter and certificates using Canva and Photoshop."
        },
        {
            "title": "Back end Developer",
            "company": "Admission team at VESIT, Mumbai",
            "duration": "June 2021-June 2022",
            "description": "Handled the entire admission process and handled the admitted students data on the admission website. Worked as backend developer and website was developed in Laravel framework."
        },
	{
            "title": "Full stack developer",
            "company": "Railway concession team at VESIT, Mumbai",
            "duration": "Dec 2021-Present",
            "description": "Developing website using HTML,CSS,JavaScript, PHP. Handling the entire online concession process and handling the students' records."
        },
	{
            "title": "Trainee Engineer",
            "company": "Kamal Sir Classes",
            "duration": "Sep 2021-Feb 2022",
            "description": " Completed Java Programming Course, Python Programming Course, MySQL course, Machine Learning & Flask Deployment course and Android Programming course."
        },
    ]
    skills = [
        "Python",
        "HTML/CSS",
        "JavaScript",
	    "Java", 
        "Android",
        "ReactJS", 
        "PHP", 
        "ML",
        "Data Analysis",
        "Data Collection",
        "Data Science", 
        "Data Visualization", 
        "Optimizing", 
        "Problem Solving", 
        "Programming", 
        "Project Management", 
        "Data Structures" 
    ]

    achievements = [
        "Winner in mask painting conducted by cultural council, VESIT",
        "Finalist in Toycathon 2021",
        "First runner up in an article writing competition conducted by CSI VESIT",
        "Second Runner up for best performer in SCIENTIA-level 1 Quiz competition",
        "Second Runner up in regard before you discard conducted by cultural council, VESIT"
    ]

    additional_info = [
        "Certifications : Introduction to Graph theory, Introduction to Structured Query language, Python Data structures.",
        "Languages : Fluent in English, Hindi and Sindhi, Basic Knowledge in Marathi and Indonesian. ",
        "Interests : Mandala , Fantasy Badminton, Data Analytics"
    ]

    return render_template('resume.html', name=name, title=title, about=about, email=email, contact_number=contact_number, LinkedIn=LinkedIn, Github=Github, education=education, experience=experience, skills=skills, academic_projects=academic_projects, internships=internships, achievements=achievements, additional_info=additional_info, hide_fields=True)

# Add a new route for the full resume page without hiding any field
@app.route('/view_full_resume')
def view_full_resume():
    name = "Radhika Katiyara"
    title = "Software Developer"
    about = "Software Engineer with an understanding of delivering high-quality software products on time and within budget and proficient in Java, Python, and JavaScript with expertise in machine learning. Unveiling insights from data."
    email = "radhika.katiyara@gmail.com"
    contact_number = "(+91)8655256117"
    LinkedIn = "https://www.linkedin.com/in/radhika-katiyara-7a958b1ab/"
    Github = "Radhika-2002"


    education = [
        {
            "school": "Smt.V.D.Gardi High School",
            "degree": "Secondary High School",
            "year": "June 2016-June 2017"
        },
	{
            "college": "SK Somaiya Vinay Madir Jr.College",
            "degree": "High Secondary,Science",
            "year": "June 2017-June 2019"
        },
	{
            "college": "Vivekanand Education Society’s Institute of Technology",
            "degree": "B.Tech, Computer Science",
            "year": "Aug 2019- May 2023"
        }
    ]
    academic_projects = [
   	{
		"project_name": "Placement Record System",
		"duration": "Aug 2019-May 2021",          	                                                                         
		"description": [
            "Analyzed and surveyed the placement process, with the team, to ensure proper management of placement records.",
            "Technologies used for building are HTML, CSS, Firebase and PHP.",
            "Downloadable reports in form of pdf.",
	    "Generates Overall Placement summary and easy search function."
        ]
	},
	{
		"project_name": "Patient Treatment Recommendation Model",
		"duration": "Aug 2021-May 2022" ,         	                                                                         
		"description": [
		"Analyzed and surveyed problem statement, with the team to advance in health technology.",
		"Technologies used for building are HTML, CSS, Python, Flask.",
		"Predicts disease according to symptoms entered and then recommends first-aid and medications to the patient.",
		"Presented and published name Title :MedEstimate: Patient Treatment Recommendation model at IEEE Xplore Digital Library (ICAST-2022).https://ieeexplore.ieee.org/document/10039522"
	]
	},
	{
		"project_name": "AI-Based Water Quality Index (WQI) Analysis of Maharashtra", 
		"duration": "Aug 2022-June 2023",         	                                                                         
		"description": [
		"Analyzed and surveyed problem statement, with the team to propose a better solution for improving WQI of Maharashtra.",
		"Proposed a portable 5G module sensor which will be useful for measuring WQI easily.",
		"Technologies used for building ML models were Python and its libraries.",
		"Received acceptance for paper International Conference on Innovative Research in Science and Technology (IRST-2023) and selected for publication in Springer Nature.",
		"Received acceptance for paper 3rd ( Proceedings by Springer and Technically associated with ACM and Namibia University of Science and Technology)  IDBA-ACMWIR-2023 and selected for publication in conference proceedings by Springer. Electronic ISSN: 2731-5568 Print ISSN: 2731-555X, Series: “Data-Intensive Research”"
	]
	}
    ]
    internships = [
        {
            "title": "Web development internship",
            "company": "The Sparks Foundation",
            "duration": "April 2021",
            "description": "In this internship I was given the task to develop a website on Payment Gateway Integration. I built this website using the following languages and technologies :HTML, CSS, razorpay. Also it was hosted on Heroku. Link: https://paymentt.herokuapp.com/"
        },
        {
            "title": "Web development internship",
            "company": "VESIT Renaissance",
            "duration": "June 2021-July 2021",
            "description": "In this internship my team was given a task to develop a website on a green credit management system. We built this website using following languages and technologies : HTML, CSS, PHP, SQL,Python"
        },
	{
            "title": "Web development internship",
            "company": "LetsGrowMore",
            "duration": "Aug 2021-Sep 2021",
            "description": "In this internship I was given 2 tasks. The first was to develop a single page website and second was to generate API’s of users using ReactJS.I built this website using following languages and technologies : HTML, CSS, ReactJS."
        }
    ]
    experience = [
        {
            "title": "Designer and editor",
            "company": "Newsletter team at VESIT, Mumbai",
            "duration": "April 2021-May 2023",
            "description": "Designing and editing newsletter and certificates using Canva and Photoshop."
        },
        {
            "title": "Back end Developer",
            "company": "Admission team at VESIT, Mumbai",
            "duration": "June 2021-June 2022",
            "description": "Handled the entire admission process and handled the admitted students data on the admission website. Worked as backend developer and website was developed in Laravel framework."
        },
	{
            "title": "Full stack developer",
            "company": "Railway concession team at VESIT, Mumbai",
            "duration": "Dec 2021-Present",
            "description": "Developing website using HTML,CSS,JavaScript, PHP. Handling the entire online concession process and handling the students' records."
        },
	{
            "title": "Trainee Engineer",
            "company": "Kamal Sir Classes",
            "duration": "Sep 2021-Feb 2022",
            "description": " Completed Java Programming Course, Python Programming Course, MySQL course, Machine Learning & Flask Deployment course and Android Programming course."
        },
    ]
    skills = [
        "Python",
        "HTML",
        "CSS",
        "JavaScript",
	    "Java", 
        "Android",
        "ReactJS", 
        "PHP", 
        "ML",
        "Data Analysis",
        "Data Collection",
        "Data Science", 
        "Data Visualization", 
        "Optimizing", 
        "Problem Solving", 
        "Programming", 
        "Project Management", 
        "Data Structures" 
    ]

    achievements = [
        "Winner in mask painting conducted by cultural council, VESIT",
        "Finalist in Toycathon 2021",
        "First runner up in an article writing competition conducted by CSI VESIT",
        "Second Runner up for best performer in SCIENTIA-level 1 Quiz competition",
        "Second Runner up in regard before you discard conducted by cultural council, VESIT"
    ]

    additional_info = [
        "Certifications : Introduction to Graph theory, Introduction to Structured Query language, Python Data structures.",
        "Languages : Fluent in English, Hindi and Sindhi, Basic Knowledge in Marathi and Indonesian. ",
        "Interests : Mandala , Fantasy Badminton, Data Analytics"
    ]
    return render_template('resume.html', name=name, title=title, about=about, email=email, contact_number=contact_number, LinkedIn=LinkedIn, Github=Github, education=education, experience=experience, skills=skills, academic_projects=academic_projects, internships=internships, achievements=achievements, additional_info=additional_info, hide_fields=False)

@app.route('/click')
def click_page():
    return render_template('click.html')

@app.route('/view_resume')
def view_resume():
    return redirect(url_for('resume'))

if __name__ == '__main__':
    app.run(debug=True)
