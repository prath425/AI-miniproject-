import nltk
from nltk.chat.util import Chat, reflections
from flask import Flask, request, render_template

app = Flask(__name__)

# Define a list of patterns and responses for the chatbot
patterns = [
    (r'Give me academic related information',
     ['Progressive Education Society Modern College of Engineering is successful in delivering high standard of education. The college offers a wide range of academic programs, including engineering, computer science, and business. The faculty is highly qualified and dedicated to providing quality education to the students.']),
    (r'Give me fee related information',
     ['The fee structure for the academic year 2023-2024 varies by program. For example, the tuition fee for the Computer Science program is $10,000 per year for in-state students and $20,000 per year for out-of-state students. Engineering students pay a different fee structure. It\'s important to check the specific program and the college\'s official website for detailed fee information.']),
]

# Create a chatbot instance
chatbot = Chat(patterns, reflections)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    responses = []

    # Check if the user input contains the word "academic"
    if 'department' in user_input:
        responses.append(
            '<div style="width: 75%; margin: 0 auto; text-align: center; font-family: Agrandir, sans-serif; background-color: #f7f7f7; padding: 20px; border-radius: 10px;">'
            '<h1 style="color: #FF5733; font-size: 36px; margin: 20px 0;">Welcome to Progressive Education Society Modern College of Engineering</h1>'
            '<p style="color: #333; font-size: 18px; margin-bottom: 20px;">Progressive Education Society Modern College of Engineering is committed to providing excellence in education and fostering innovation. We offer a diverse range of academic programs that prepare students for successful careers in various fields. Explore our programs:</p>'
            '<ul style="list-style-type: disc; padding-left: 20px;">'
            '<li style="color: #007BFF; font-size: 20px; margin: 10px 0;">Bachelor of Engineering (B.E.) - A comprehensive undergraduate program for future engineers.</li>'
            '<li style="color: #28a745; font-size: 20px; margin: 10px 0;">Master of Engineering (M.E.) - Advance your engineering skills and knowledge.</li>'
            '<li style="color: #FF5733; font-size: 20px; margin: 10px 0;">Bachelor of Technology (B.Tech) - Stay at the forefront of technology and innovation.</li>'
            '<li style="color: #28a745; font-size: 20px; margin: 10px 0;">Master of Technology (M.Tech) - Take your technical expertise to the next level.</li>'
            '<li style="color: #007BFF; font-size: 20px; margin: 10px 0;">Bachelor of Computer Applications (BCA) - Explore the world of computer science and applications.</li>'
            '<li style="color: #28a745; font-size: 20px; margin: 10px 0;">Master of Computer Applications (MCA) - Master the art of computer science and applications.</li>'
            '<li style="color: #007BFF; font-size: 20px; margin: 10px 0;">Bachelor of Science (B.Sc.) in Computer Science - Dive into the world of computer science.</li>'
            '<li style="color: #28a745; font-size: 20px; margin: 10px 0;">Master of Science (M.Sc.) in Computer Science - Take your computer science skills to the next level.</li>'
            '<li style="color: #FF5733; font-size: 20px; margin: 10px 0;">Bachelor of Business Administration (BBA) - Prepare for a successful career in business and management.</li>'
            '<li style="color: #28a745; font-size: 20px; margin: 10px 0;">Master of Business Administration (MBA) - Advance your business and management skills with our MBA program.</li>'
            '</ul>'
            '<p style="color: #333; font-size: 18px; margin: 20px 0;">Our academic programs are designed to provide a high standard of education and ensure that students are well-prepared for their future careers. The faculty at our college is highly qualified and dedicated to providing quality education. They bring expertise and real-world experience to the classroom, enriching the learning experience.</p>'
            '<p style="color: #333; font-size: 18px; margin: 20px 0;">In addition to academic excellence, we also offer a range of extracurricular activities, student organizations, and opportunities for personal and professional development. We believe in nurturing well-rounded individuals who are ready to make a positive impact on the world.</p>'
            '<p style="color: #333; font-size: 18px; margin: 20px 0;">Whether you\'re a prospective student or a member of our college community, we\'re excited to have you with us on this journey of learning and growth. Explore our website for more information and feel free to reach out to us with any questions you may have.</p>'
            '</div>'

        )

        # Check if the user input contains the word "fee"
    if 'fee' in user_input:
        responses.append(
            '<div style="width: 75%; margin: 0 auto; text-align: left; font-family: Agrandir, sans-serif; background-color: #f7f7f7; padding: 20px; border-radius: 10px;">'
            '<h1 style="color: #FF5733; font-size: 36px; margin: 20px 0;">Fee structure</h1>'

            '<p style="color: #333; font-size: 18px; margin: 20px 0;">The fee structure for the academic year 2023-2024 varies by program:</p>'
            '<ul style="list-style-type: disc; padding-left: 20px;">'
            '<li style="font-weight: bold;">Computer Science program:</li>'
            '<ul style="list-style-type: circle; padding-left: 20px;">'
            '<li>In-state students: Rs.10,000 per year</li>'
            '<li>Out-of-state students: Rs.20,000 per year</li>'
            '</ul>'
            '<li style="font-weight: bold;">Engineering program (Please check the program for specific details):</li>'
            '<ul style="list-style-type: circle; padding-left: 20px;">'
            '<li>The Engineering programs fee structure can differ depending on the specific branch of engineering you choose, such as Mechanical, Electrical, or Civil Engineering.</li>'
            '<li>Specific fees for the Engineering program may be subject to change and can depend on factors like the number of credits, course materials, and any additional program-related fees.</li>'
            '</ul>'
            '</ul>'
            '<p style="color: #333; font-size: 18px;">It is essential to check the specific program and the college\'s official website for detailed and up-to-date fee information:</p>'
            '<ul style="list-style-type: disc; padding-left: 20px;">'
            '<li>Tuition fees may be adjusted annually, so it\'s recommended to verify the latest fee rates for accurate financial planning.</li>'
            '<li>In addition to tuition, students should also consider other expenses, such as textbooks, housing, and living costs when budgeting for their education.</li>'
            '<li>Financial aid and scholarship opportunities may be available to help offset the cost of education. It is advisable to explore these options and their application deadlines to secure potential financial assistance.</li>'
            '<li>Some programs may offer part-time or co-op opportunities, which can provide students with income to help cover their educational expenses while gaining valuable work experience.</li>'
            '<li>Our college is dedicated to helping students make informed decisions about their education and finances. If you have any questions or need further assistance, please feel free to reach out to our financial aid office.</li>'
            '<li>We understand the importance of managing educational expenses and are here to support your journey towards a successful and affordable education.</li>'
            '</ul>'
            '</div>'

        )

    if 'FAQ' in user_input:
        responses.append(
            '<div style="width: 75%; margin: 0 auto; text-align: left; font-family: Agrandir, sans-serif; background-color: #f7f7f7; padding: 20px; border-radius: 10px;">'
    '<h1 style="color: #FF5733; font-size: 36px; margin: 20px 0;">Frequently Asked Questions</h1>'

    '<p style="color: #333; font-size: 18px; margin: 20px 0;">The admission process for this college may vary depending on the program and institution:</p>'
    '<ul style="list-style-type: disc; padding-left: 20px;">'
    '<li><strong>Q1:</strong> What is the admission process for this college?</li>'
    '<p><strong>A1:</strong> The admission process typically involves submitting an online application, providing required documents such as transcripts and test scores, and possibly attending an interview or entrance exam. Specific requirements may vary by program and institution.</p>'
    '<li><strong>Q2:</strong> What are the tuition and fees for this college?</li>'
    '<p><strong>A2:</strong> Tuition and fees can vary widely depending on the college, the program of study, and whether you are an in-state or out-of-state student. It\'s best to check the college\'s official website or contact the admissions office for the most accurate and up-to-date information.</p>'
    '<li><strong>Q3:</strong> Are there scholarships or financial aid options available?</li>'
    '<p><strong>A3:</strong> Many colleges offer scholarships and financial aid packages to eligible students. These may be based on academic achievement, financial need, or specific talents. You can find information on available scholarships and financial aid on the college\'s website or by contacting their financial aid office.</p>'
    '<li><strong>Q4:</strong> Can I work part-time while studying at this college?</li>'
    '<p><strong>A4:</strong> Some colleges allow international or domestic students to work part-time on or off-campus. However, there are often restrictions and guidelines, so it\'s essential to check with the college.</p>'
    '<li><strong>Q5:</strong> What is the application deadline for admission?</li>'
    '<p><strong>A5:</strong> Application deadlines can vary by program and term. It\'s important to check the specific program or department\'s website for the most accurate deadline information.</p>'
    '<li><strong>Q6:</strong> Is there an entrance exam requirement for all programs?</li>'
    '<p><strong>A6:</strong> Entrance exam requirements can vary by program. Some programs may require entrance exams such as the GRE or GMAT, while others may not. Check the program\'s admission requirements for details.</p>'
    '</ul>'
    '<p style="color: #333; font-size: 18px;">For more detailed and program-specific admission information, please refer to the official college website or contact the admissions office.</p>'
    '</div>')


    if 'scholarship details' in user_input:
        responses.append(
            '<div style="width: 75%; text-align: left; font-family: Agrandir, sans-serif; background-color: #ECECEC; padding: 20px; border-radius: 10px;">'
            '<h1 style="color: #FF5733; font-size: 36px; margin: 20px 0;">Scholarships at this college</h1>'
            '<ul style="list-style-type: disc; padding-left: 20px;">'
            '<li>Academic Excellence Scholarship: Awarded to students with exceptional academic records.</li>'
            '<li>Need-Based Financial Aid: Designed to assist students with demonstrated financial need.</li>'
            '<li>STEM Scholarships: Available for students pursuing degrees in science, technology, engineering, and mathematics.</li>'
            '</ul>'
            '<p style="color: #333; font-size: 18px; margin: 20px 0;">To explore available scholarships and get a complete list, visit the college\'s official scholarship page or contact the financial aid office.</p>'
            '<p style="color: #333; font-size: 18px; margin: 20px 0;">To apply for scholarships at this college:</p>'
            '<ol style="list-style-type: decimal; padding-left: 20px;">'
            '<li>Visit the college\'s scholarship page on their official website to explore available scholarship opportunities.</li>'
            '<li>Complete the scholarship application(s) for the scholarships you\'re interested in. Pay attention to application deadlines and requirements, as they may vary.</li>'
            '<li>Some scholarships may require additional materials, such as essays, letters of recommendation, or a portfolio. Make sure to provide the necessary information as requested.</li>'
            '</ol>'
            '<p style="color: #333; font-size: 18px; margin: 20px 0;">International students can also benefit from scholarships at this college, including:</p>'
            '<ul style="list-style-type: disc; padding-left: 20px;">'
            '<li>International Merit Scholarship: Awarded to outstanding international students based on academic achievements and extracurricular involvement.</li>'
            '<li>Global Diversity Scholarship: Aimed at promoting diversity on campus by supporting international students from various backgrounds.</li>'
            '</ul>'
            '<p style="color: #333; font-size: 18px; margin: 20px 0;">For more information on scholarships for international students, visit the college\'s official scholarship page or reach out to the international student services office.</p>'
            '<p style="color: #333; font-size: 18px; margin: 20px 0;">Scholarship application deadlines can vary, so it\'s important to check the deadline for each scholarship opportunity you\'re interested in. These deadlines may not align with the college\'s admission application deadlines, so be sure to check the scholarship details on the college\'s website.</p>'
                         '<p style="color: #333; font-size: 18px; margin: 20px 0;">Students often have the flexibility to combine multiple scholarships at this college to support their education. However, there may be limitations or restrictions depending on the scholarship policies. Be sure to review the terms and conditions of each scholarship to determine if they can be combined. If you have questions about combining scholarships, seek guidance from the financial aid office for more information.</p>'
                         '</div>'



        )

    if 'admission details' in user_input:
        responses.append(
            '<div style="width: 100%; margin: 0 auto; text-align: left; font-family: Agrandir, sans-serif; background-color: #f7f7f7; padding: 20px; border-radius: 10px;">'
    '<h1 style="color: #FF5733; font-size: 36px; margin: 20px 0;">Admission Details for this college:</h1>'
    
    '<ul style="list-style-type: disc; padding-left: 20px;">'
        '<li>Application Requirements: Applicants are typically required to submit the following materials when applying for admission:</li>'
        '<ul style="list-style-type: circle; padding-left: 20px;">'
            '<li>Completed Application Form: This can usually be found on the college\'s official website.</li>'
            '<li>Transcripts: High school transcripts or transcripts from previous academic institutions are often required for undergraduate applicants. Graduate applicants may need to provide transcripts from their bachelor\'s degree programs.</li>'
            '<li>Standardized Test Scores: Some colleges require SAT or ACT scores for undergraduate admissions, while graduate programs may require GRE or other relevant test scores. Be sure to check the specific requirements for your intended program.</li>'
            '<li>Letters of Recommendation: Most graduate programs and some undergraduate programs ask for letters of recommendation from teachers, professors, or employers. Check the college\'s website for details on the number and source of required recommendations.</li>'
            '<li>Admission Essays or Personal Statements: Some colleges may ask for a personal statement or essay outlining your academic and personal goals, as well as your reasons for choosing the college.</li>'
            '<li>Application Fee: Be prepared to pay an application fee, which can vary from one college to another. Check the specific fee and payment methods on the college\'s application portal.</li>'
        '</ul>'
        '<li>Application Deadlines: The college typically has application deadlines for different admission rounds. Common deadlines include Early Decision, Regular Decision, and Rolling Admissions. Be sure to submit your application before the specified deadline to be considered for admission.</li>'
        '<li>Notification of Admission: After submitting your application, the college will review it and notify you of their admission decision. Notification dates can vary, so check the college\'s official website or your application portal for updates.</li>'
        '<li>Financial Aid and Scholarships: The college offers a range of financial aid options, including scholarships, grants, and loans. Visit the college\'s financial aid page for details on how to apply and the types of financial aid available.</li>'
    '</ul>'
    
    '<li>International Students: If you\'re an international student, additional requirements may apply. These could include English language proficiency tests like TOEFL or IELTS, visa documentation, and proof of financial support. Visit the international admissions page on the college\'s website for specific information.</li>'
    
    '<li>Transfer Students: If you\'re transferring from another college or university, the admission requirements for transfer students may differ. Contact the college\'s admissions office or visit the transfer admissions page on their website for details.</li>'
    
    '<li>Additional Information: For more comprehensive admission details, including program-specific requirements and contact information for the admissions office, please visit the official college website or get in touch with the admissions office directly.</li>'
'</div>'

        )

    # If neither "academic" nor "fee" is mentioned, use the chatbot to respond
    if not responses:
        responses.extend(chatbot.respond(user_input))

    return '\n'.join(responses)

if __name__ == '__main__':
    app.run(debug=True)
