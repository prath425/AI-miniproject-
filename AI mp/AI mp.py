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
            '<ul>'
            '<li>The Progressive Education Society Modern College of Engineering offers a diverse range of academic programs, including:</li>'
            '<ul>'
            '<li>1. Bachelor of Engineering (B.E.)</li>'
            '<li>2. Master of Engineering (M.E.)</li>'
            '<li>3. Bachelor of Technology (B.Tech)</li>'
            '<li>4. Master of Technology (M.Tech)</li>'
            '<li>5. Bachelor of Computer Applications (BCA)</li>'
            '<li>6. Master of Computer Applications (MCA)</li>'
            '<li>7. Bachelor of Science (B.Sc.) in Computer Science</li>'
            '<li>8. Master of Science (M.Sc.) in Computer Science</li>'
            '<li>9. Bachelor of Business Administration (BBA)</li>'
            '<li>10. Master of Business Administration (MBA)</li>'
            '</ul>'
            '<li>The colleges academic programs are designed to provide a high standard of education and preparestudents for successful careers. </ li > '
        '<li>The faculty at the college is highly qualified and dedicated to providing quality education. They bring expertise and experience to the classroom, enriching the learning experience.</li>'
        '</ul>'
        )

    # Check if the user input contains the word "fee"
    if 'fee' in user_input:
        responses.append(
            '<ul>'
            '<li>The fee structure for the academic year 2023-2024 varies by program:</li>'
            '<ul>'
            '<li>1. Computer Science program:'
            '<ul>'
            '<li>- In-state students: Rs.10,000 per year</li>'
            '<li>- Out-of-state students: Rs.20,000 per year</li>'
            '</ul>'
            '<li>2. Engineering program (Please check the program for specific details):</li>'
            '<ul>'
            '<li>- The Engineering programs fee structure can differ depending on the specific branch of engineering you choose, such as Mechanical, Electrical, or Civil Engineering. < / li > '
                              '<li>- Specific fees for the Engineering program may be subject to change and can depend on factors like the number of credits, course materials, and any additional program-related fees.</li>'
                              '</ul>'
                              '</ul>'
                              '<li>It is essential to check the specific program and the college\'s official website for detailed and up-to-date fee information:</li>'
                              '<ul>'
                              '<li>- Tuition fees may be adjusted annually, so it s  recommended  to  verify  thelatestfee rates for accurate financial planning.< / li > '
        '<li>- In addition to tuition, students should also consider other expenses, such as textbooks, housing, and living costs, when budgeting for their education.</li>'
        '<li>- Financial aid and scholarship opportunities may be available to help offset the cost of education. It is advisable to explore these options and their application deadlines to secure potential financial assistance.</li>'
        '<li>- Some programs may offer part-time or co-op opportunities, which can provide students with income to help cover their educational expenses while gaining valuable work experience.</li>'
        '</ul>'
        '</ul>'
        )

    if 'FAQ' in user_input:
        responses.append(
            '<ul>'
            '<li><strong>Q1:</strong> What is the admission process for this college?</li>'
            '<p><strong>A1:</strong> The admission process typically involves submitting an online application, providing required documents such as transcripts and test scores, and possibly attending an interview or entrance exam. Specific requirements may vary by program and institution.</p>'
            '<li><strong>Q2:</strong> What are the tuition and fees for this college?</li>'
            '<p><strong>A2:</strong> Tuition and fees can vary widely depending on the college, the program of study, and whether you are an in-state or out-of-state student. It\'s best to check the college\'s official website or contact the admissions office for the most accurate and up-to-date information.</p>'
            '<li><strong>Q3:</strong> Are there scholarships or financial aid options available?</li>'
            '<p><strong>A3:</strong> Many colleges offer scholarships and financial aid packages to eligible students. These may be based on academic achievement, financial need, or specific talents. You can find information on available scholarships and financial aid on the college\'s website or by contacting their financial aid office.</p>'
            '<li><strong>Q4:</strong> Can I work part-time while studying at this college?</li>'
            '<p><strong>A4:</strong> Some colleges allow international or domestic students to work part-time on or off-campus. However, there are often restrictions and guidelines, so it\'s essential to check with the college.</p>'
            '<li><strong>Q5:</strong> What is the application deadline for admission?</li>'
            '<p><strong>A5:</strong> Application deadlines can vary by program and term. Its important to check the  specific program or departments website for the most accurate deadline information.</p>'
        '<li><strong>Q6:</strong> Is there an entrance exam requirement for all programs?</li>'
        '<p><strong>A6:</strong> Entrance exam requirements can vary by program. Some programs may require entrance exams such as the GRE or GMAT, while others may not. Check the programs admission requirementsfor details.< / p > '
        '</ul>'
        )
    if 'scholarship details' in user_input:
        responses.append(
            '<ul>'
            '<li>Scholarships at this college:</li>'
            '<ul>'
            '<li>Academic Excellence Scholarship: Awarded to students with exceptional academic records.</li>'
            '<li>Need-Based Financial Aid: Designed to assist students with demonstrated financial need.</li>'
            '<li>STEM Scholarships: Available for students pursuing degrees in science, technology, engineering, and mathematics.</li>'
            '</ul>'
            '<li>To explore available scholarships and get a complete list, visit the college\'s official scholarship page or contact the financial aid office.</li>'
            '<li>To apply for scholarships at this college:</li>'
            '<ol>'
            '<li>Visit the college\'s scholarship page on their official website to explore available scholarship opportunities.</li>'
            '<li>Complete the scholarship application(s) for the scholarships you\'re interested in. Pay attention to application deadlines and requirements, as they may vary.</li>'
            '<li>Some scholarships may require additional materials, such as essays, letters of recommendation, or a portfolio. Make sure to provide the necessary information as requested.</li>'
            '</ol>'
            '<li>International students can also benefit from scholarships at this college, including:</li>'
            '<ul>'
            '<li>International Merit Scholarship: Awarded to outstanding international students based on academic achievements and extracurricular involvement.</li>'
            '<li>Global Diversity Scholarship: Aimed at promoting diversity on campus by supporting international students from various backgrounds.</li>'
            '</ul>'
            '<li>For more information on scholarships for international students, visit the college\'s official scholarship page or reach out to the international student services office.</li>'
            '<li>Scholarship application deadlines can vary, so it\'s important to check the deadline for each scholarship opportunity you\'re interested in. These deadlines may not align with the college\'s admission application deadlines, so be sure to check the scholarship details on the college\'s website.</li>'
            '<li>Students often have the flexibility to combine multiple scholarships at this college to support their education. However, there may be limitations or restrictions depending on the scholarship policies. Be sure to review the terms and conditions of each scholarship to determine if they can be combined. If you have questions about combining scholarships, seek guidance from the financial aid office for more information.</li>'
            '</ul>'
        )
    if 'admission details' in user_input:
         responses.append(
                '<ul>'
                '<li>Admission Details for this college:</li>'
                '<ul>'
                '<li>Application Requirements: Applicants are typically required to submit the following materials when applying for admission:</li>'
                '<ul>'
                '<li>Completed Application Form: This can usually be found on the college\'s official website.</li>'
                '<li>Transcripts: High school transcripts or transcripts from previous academic institutions are often required for undergraduate applicants. Graduate applicants may need to provide transcripts from their bachelor\'s degree programs.</li>'
                '<li>Standardized Test Scores: Some colleges require SAT or ACT scores for undergraduate admissions, while graduate programs may require GRE or other relevant test scores. Be sure to check the specific requirements for your intended program.</li>'
                '<li>Letters of Recommendation: Most graduate programs and some undergraduate programs ask for letters of recommendation from teachers, professors, or employers. Check the college\'s website for details on the number and source of required recommendations.</li>'
                '<li>Admission Essays or Personal Statements: Some colleges may ask for a personal statement or essay outlining your academic and personal goals, as well as your reasons for choosing the college.</li>'
                '<li>Application Fee: Be prepared to pay an application fee, which can vary from one college to another. Check the specific fee and payment methods on the college\'s application portal.</li>'
                '</ul>'
                '<li>Application Deadlines: The college typically has application deadlines for different admission rounds. Common deadlines include Early Decision, Regular Decision, and Rolling Admissions. Be sure to submit your application before the specified deadline to be considered for admission.</li>'
                '<li>Notification of Admission: After submitting your application, the college will review it and notify you of their admission decision. Notification dates can vary, so check the colleges   official  website or your application portal for updates.< / li > '
                '<li>Financial Aid and Scholarships The college offers a range of financial aid options, including scholarships, grants, and loans. Visit the colleges financial aid page for details on how to apply and the types of financial aid available.</li>'
            '</ul>'
            '<li>International Students: If youre an international student, additional requirements may apply.These could include English language proficiency tests like TOEFL or IELTS, visa documentation, and proof of financial support.Visit the international admissions page on the colleges website for specific information.</li>'
            '<li>Transfer Students: If youre transferring from another college or university, the admission requirements for transfer students may differ.Contact the colleges admissions office or visit the transfer admissions page on their website for details.</li>'
            '<li>Additional Information: For more comprehensive admission details, including program-specific requirements and contact information for the admissions office, please visit the official college website or get in touch with the admissions office directly.</li>'
            '</ul>'
            )

    # If neither "academic" nor "fee" is mentioned, use the chatbot to respond
    if not responses:
        responses.extend(chatbot.respond(user_input))

    return '\n'.join(responses)


if __name__ == '__main__':
    app.run(debug=True)
