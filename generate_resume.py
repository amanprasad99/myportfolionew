import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, ListFlowable, ListItem
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT

def create_resume(filename):
    # Setup document geometry (0.4 inch margins)
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        leftMargin=30,
        rightMargin=30,
        topMargin=30,
        bottomMargin=30
    )
    
    story = []
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=22,
        leading=26,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#000000'),
        spaceAfter=6
    )
    
    contact_style = ParagraphStyle(
        'ContactInfo',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=12,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#222222'),
        spaceAfter=8
    )
    
    section_heading = ParagraphStyle(
        'SectionHeading',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=15,
        textColor=colors.HexColor('#000000'),
        spaceBefore=8,
        spaceAfter=2
    )
    
    body_style = ParagraphStyle(
        'BodyTextCustom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13,
        textColor=colors.HexColor('#111111'),
        spaceAfter=4
    )
    
    bullet_style = ParagraphStyle(
        'BulletCustom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13,
        textColor=colors.HexColor('#111111'),
        leftIndent=15,
        spaceAfter=2
    )

    # 1. Header Name
    story.append(Paragraph("Aman Prasad", title_style))
    
    # Contact Links
    contact_text = (
        "&nbsp;&nbsp;✉ amanprasad38649@gmail.com &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
        "🔗 linkedin.com/in/aman-prasad99 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
        "💻 github.com/amanprasad99"
    )
    story.append(Paragraph(contact_text, contact_style))
    story.append(HRFlowable(width="100%", thickness=0.8, color=colors.HexColor('#333333'), spaceBefore=2, spaceAfter=8))
    
    # 2. Profile Summary
    story.append(Paragraph("Profile Summary", section_heading))
    summary_text = (
        "Motivated and dedicated Computer Science Engineering student with a strong foundation in Java, JavaScript, Data "
        "Structures and Algorithms, and web development. Passionate about building practical software solutions and continuously "
        "improving problem-solving and programming skills. Familiar with developing projects using modern technologies "
        "and actively preparing for software development and placement opportunities. Eager to contribute technical skills, learn "
        "new technologies, and grow as a software developer."
    )
    story.append(Paragraph(summary_text, body_style))
    
    # 3. Education
    story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#888888'), spaceBefore=6, spaceAfter=4))
    story.append(Paragraph("Education", section_heading))
    
    edu_1 = (
        "<b>Bachelor of Technology (Computer Science and Engineering)</b>"
        "<font color='#555555'> &nbsp;&nbsp;—&nbsp;&nbsp; Chandigarh Engineering Colleges, Jhanjeri</font>"
        "<font color='#333333'> (2024 – 2028)</font><br/>"
        "<b>CGPA:</b> 7.5"
    )
    story.append(Paragraph(edu_1, body_style))
    
    edu_2 = (
        "<b>Senior Secondary Education (XII)</b>"
        "<font color='#555555'> &nbsp;&nbsp;—&nbsp;&nbsp; R.L.S.Y College Bettiah, Bihar</font>"
        "<font color='#333333'> (2023)</font><br/>"
        "<b>Percentage:</b> 74%"
    )
    story.append(Paragraph(edu_2, body_style))

    edu_3 = (
        "<b>Secondary Education (X)</b>"
        "<font color='#555555'> &nbsp;&nbsp;—&nbsp;&nbsp; R.K.V.V.M School Bettiah, Bihar</font>"
        "<font color='#333333'> (2021)</font><br/>"
        "<b>Percentage:</b> 84%"
    )
    story.append(Paragraph(edu_3, body_style))

    # 4. Projects
    story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#888888'), spaceBefore=6, spaceAfter=4))
    story.append(Paragraph("Projects", section_heading))
    
    # Project 1
    story.append(Paragraph("<b>Smart Medicine Reminder System</b>", ParagraphStyle('SubHeading', parent=body_style, fontName='Helvetica-Bold', fontSize=10, leading=13)))
    story.append(Paragraph("• Developed a reminder application for managing medication schedules with timely notifications.", bullet_style))
    story.append(Paragraph("• Built an IoT prototype with ESP32, DS3231 RTC, LCD, buzzer, and buttons for scheduled reminders and missed-dose tracking.", bullet_style))
    story.append(Paragraph("• <b>Tech Stack:</b> ESP32, Arduino, DS3231 RTC, LCD, C/C++", bullet_style))
    story.append(Spacer(1, 4))
    
    # Project 2
    story.append(Paragraph("<b>TempChat — Real-Time 1-to-1 Chat Application</b>", ParagraphStyle('SubHeading', parent=body_style, fontName='Helvetica-Bold', fontSize=10, leading=13)))
    story.append(Paragraph("• Designed a private chat application with authentication, real-time messaging, and image/video sharing.", bullet_style))
    story.append(Paragraph("• Implemented a WhatsApp-style interface with online/offline status, typing indicator, and delivered/seen message states.", bullet_style))
    story.append(Paragraph("• <b>Tech Stack:</b> Next.js, React.js, Node.js, Supabase, JavaScript", bullet_style))
    story.append(Spacer(1, 4))

    # Project 3
    story.append(Paragraph("<b>Hospital Management System</b>", ParagraphStyle('SubHeading', parent=body_style, fontName='Helvetica-Bold', fontSize=10, leading=13)))
    story.append(Paragraph("• Developed a responsive Hospital Management System to streamline patient, doctor, and appointment management.", bullet_style))
    story.append(Paragraph("• Implemented modules for patient registration, doctor management, appointment scheduling, and medical records states.", bullet_style))
    story.append(Paragraph("• Designed a user-friendly interface with HTML, CSS, JavaScript and responsive layouts.", bullet_style))
    story.append(Paragraph("• <b>Tech Stack:</b> HTML, CSS, JavaScript, Responsive Layouts", bullet_style))

    # 5. Skills
    story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#888888'), spaceBefore=6, spaceAfter=4))
    story.append(Paragraph("Skills", section_heading))
    story.append(Paragraph("• <b>Technical Skills:</b> C++, Java, HTML, CSS, JavaScript, C++ STL, Node.js (Basics), Express.js (Basics), Git, GitHub, MySQL, MongoDB", bullet_style))
    story.append(Paragraph("• <b>Soft Skills:</b> Leadership, Problem Solving, Teamwork, Communication, Adaptability, Time Management", bullet_style))
    story.append(Paragraph("• <b>CS Concepts:</b> Data Structures & Algorithms, Object-Oriented Programming, Operating Systems, DBMS, Computer Networks, Computer Organization and Architecture", bullet_style))

    # 6. Achievements & Leadership
    story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#888888'), spaceBefore=6, spaceAfter=4))
    story.append(Paragraph("Achievements & Leadership", section_heading))
    story.append(Paragraph("• Participated in Project Showcase during the College Fest, presenting academic projects and explaining technical implementation.", bullet_style))
    story.append(Paragraph("• Participated in College Science Day and received a Certificate of Participation.", bullet_style))

    # 7. Certifications
    story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#888888'), spaceBefore=6, spaceAfter=4))
    story.append(Paragraph("Certifications", section_heading))
    story.append(Paragraph("• <b>Java Programming Fundamentals</b> — Infosys Springboard", bullet_style))
    story.append(Paragraph("• <b>Python Certification</b> — Infosys Springboard", bullet_style))
    story.append(Paragraph("• <b>AWS Cloud Foundations</b> — AWS Academy", bullet_style))

    doc.build(story)

if __name__ == '__main__':
    create_resume('Resume.pdf')
    create_resume('public/Resume.pdf')
    create_resume('dist/Resume.pdf')
    print("Resume PDFs generated successfully!")
