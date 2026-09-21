from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

pdf_path = "public/resume.pdf"
doc = SimpleDocTemplate(
    pdf_path,
    pagesize=letter,
    leftMargin=0.5 * inch,
    rightMargin=0.5 * inch,
    topMargin=0.4 * inch,
    bottomMargin=0.4 * inch
)

styles = getSampleStyleSheet()

name_style = ParagraphStyle(
    'Name',
    parent=styles['Heading1'],
    fontName='Helvetica-Bold',
    fontSize=20,
    leading=22,
    alignment=1, # Center
    textColor=colors.HexColor('#111827'),
    spaceAfter=4
)

contact_style = ParagraphStyle(
    'Contact',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=9,
    leading=12,
    alignment=1, # Center
    textColor=colors.HexColor('#374151'),
    spaceAfter=8
)

section_style = ParagraphStyle(
    'SectionHeading',
    parent=styles['Heading2'],
    fontName='Helvetica-Bold',
    fontSize=11,
    leading=13,
    textColor=colors.HexColor('#111827'),
    spaceBefore=6,
    spaceAfter=2
)

job_title_style = ParagraphStyle(
    'JobTitle',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=9.5,
    leading=12,
    textColor=colors.HexColor('#111827')
)

job_meta_style = ParagraphStyle(
    'JobMeta',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=9,
    leading=12,
    alignment=2, # Right
    textColor=colors.HexColor('#4B5563')
)

job_sub_style = ParagraphStyle(
    'JobSub',
    parent=styles['Normal'],
    fontName='Helvetica-Oblique',
    fontSize=9,
    leading=11.5,
    textColor=colors.HexColor('#374151'),
    spaceAfter=2
)

bullet_style = ParagraphStyle(
    'Bullet',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=8.5,
    leading=11,
    leftIndent=12,
    firstLineIndent=-8,
    textColor=colors.HexColor('#1F2937'),
    spaceAfter=2
)

skill_label_style = ParagraphStyle(
    'SkillLabel',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=8.5,
    leading=11.5,
    textColor=colors.HexColor('#111827')
)

skill_val_style = ParagraphStyle(
    'SkillVal',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=8.5,
    leading=11.5,
    textColor=colors.HexColor('#374151')
)

elements = []

# Header
elements.append(Paragraph("Jerry (Ruiyang) Ji", name_style))
elements.append(Paragraph("707-849-2690 &nbsp;|&nbsp; rj378@cornell.edu &nbsp;|&nbsp; linkedin.com/in/ruiyangji &nbsp;|&nbsp; github.com/ruiyangji", contact_style))
elements.append(HRFlowable(width="100%", thickness=0.75, color=colors.HexColor('#9CA3AF'), spaceBefore=1, spaceAfter=4))

# Education
elements.append(Paragraph("Education", section_style))
elements.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#D1D5DB'), spaceBefore=1, spaceAfter=3))

edu_table_data = [
    [Paragraph("<b>Cornell University</b> &mdash; Ithaca, NY", job_title_style), Paragraph("Aug 2023 &ndash; Dec 2026", job_meta_style)],
    [Paragraph("<i>Bachelor of Science in Computer Science</i> &nbsp;|&nbsp; <b>GPA: 3.8</b>", job_sub_style), Paragraph("", job_meta_style)]
]
t_edu = Table(edu_table_data, colWidths=[5.0*inch, 2.5*inch])
t_edu.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('BOTTOMPADDING', (0,0), (-1,-1), 0), ('TOPPADDING', (0,0), (-1,-1), 0)]))
elements.append(t_edu)

elements.append(Paragraph("<b>Relevant Coursework:</b> Distributed Systems, Operating Systems, Machine Learning, Deep Learning, Parallel Computing, Database Management, Computer Networks, Data Structures", bullet_style))
elements.append(Spacer(1, 4))

# Experience
elements.append(Paragraph("Experience", section_style))
elements.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#D1D5DB'), spaceBefore=1, spaceAfter=3))

# Meta
meta_data = [
    [Paragraph("<b>Meta</b> &mdash; Software Engineering Intern | <i>Capacity Efficiency</i>", job_title_style), Paragraph("May 2026 &ndash; Aug 2026 &bull; Menlo Park, CA", job_meta_style)]
]
t_meta = Table(meta_data, colWidths=[5.2*inch, 2.3*inch])
t_meta.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('BOTTOMPADDING', (0,0), (-1,-1), 0), ('TOPPADDING', (0,0), (-1,-1), 0)]))
elements.append(t_meta)
elements.append(Paragraph("&bull; Shipped <b>150+ production diffs</b> across 3 core milestones, independently scoping and architecting scalable backend features while leveraging AI developer tools to accelerate delivery cycles.", bullet_style))
elements.append(Paragraph("&bull; Increased review adoption from <b>10% to 70%</b> across 3 orgs by engineering an automated <b>Chronos evaluation pipeline</b> to backtest 2,000+ historical capacity optimization proposals.", bullet_style))
elements.append(Paragraph("&bull; Boosted evaluation accuracy by <b>20%</b> by adapting SkillOpt from Microsoft research and implementing automated reflection agent execution workflows for multi-step reasoning.", bullet_style))
elements.append(Paragraph("&bull; Scaled review workflows on the Efficiency Hero platform for <b>3,000+ engineers</b>, enabling automated validation and auditing of <b>$300M+</b> in quarterly compute savings.", bullet_style))
elements.append(Spacer(1, 3))

# PayPal
paypal_data = [
    [Paragraph("<b>PayPal</b> &mdash; Software Engineering Intern | <i>Backend</i>", job_title_style), Paragraph("May 2025 &ndash; Aug 2025 &bull; San Jose, CA", job_meta_style)]
]
t_paypal = Table(paypal_data, colWidths=[5.2*inch, 2.3*inch])
t_paypal.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('BOTTOMPADDING', (0,0), (-1,-1), 0), ('TOPPADDING', (0,0), (-1,-1), 0)]))
elements.append(t_paypal)
elements.append(Paragraph("&bull; Engineered <b>5+ production-ready backend features</b> for core billing and subscription services by collaborating cross-functionally across Agile sprints with QA, product, and frontend teams.", bullet_style))
elements.append(Paragraph("&bull; Extended 10+ legacy API endpoints to support <b>20+ downstream microservices</b>, ensuring strict idempotency, contract compliance, and zero backward-compatibility regressions.", bullet_style))
elements.append(Paragraph("&bull; Diagnosed and resolved distributed latency and failure bottlenecks across <b>8 services</b> using end-to-end distributed tracing, request context propagation, and logging telemetry.", bullet_style))
elements.append(Paragraph("&bull; Elevated SonarQube code quality score from <b>75 to 90</b> by expanding unit and integration test suites and refactoring 20+ core service classes with standard Java design patterns.", bullet_style))
elements.append(Spacer(1, 3))

# Cornell CMSX
cmsx_data = [
    [Paragraph("<b>Cornell Course Management System X</b> &mdash; <i>Full Stack Software Engineer</i>", job_title_style), Paragraph("Sep 2023 &ndash; Apr 2024 &bull; Ithaca, NY", job_meta_style)]
]
t_cmsx = Table(cmsx_data, colWidths=[5.2*inch, 2.3*inch])
t_cmsx.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('BOTTOMPADDING', (0,0), (-1,-1), 0), ('TOPPADDING', (0,0), (-1,-1), 0)]))
elements.append(t_cmsx)
elements.append(Paragraph("&bull; Maintained a <b>20+ year legacy codebase (100k+ LoC in Java)</b> for <b>8,000+ active students</b> by collaborating in Agile sprints, conducting rigorous code reviews, and resolving technical debt.", bullet_style))
elements.append(Paragraph("&bull; Optimized server-side memory usage and reduced backend response times by <b>15%</b> by refactoring high-latency database queries and entity relationships utilizing Java WildFly and Jakarta JPA.", bullet_style))
elements.append(Spacer(1, 4))

# Projects
elements.append(Paragraph("Projects", section_style))
elements.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#D1D5DB'), spaceBefore=1, spaceAfter=3))

# RL Cluster Scheduler
rl_data = [
    [Paragraph("<b>RL Cluster Scheduler</b> &nbsp;|&nbsp; <i>Python, PyTorch, Gymnasium, PPO</i>", job_title_style), Paragraph("Jan 2026 &ndash; Present", job_meta_style)]
]
t_rl = Table(rl_data, colWidths=[5.5*inch, 2.0*inch])
t_rl.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('BOTTOMPADDING', (0,0), (-1,-1), 0), ('TOPPADDING', (0,0), (-1,-1), 0)]))
elements.append(t_rl)
elements.append(Paragraph("&bull; Built a discrete-event simulator to train RL agents for job scheduling; utilized <b>Action Masking</b> to enforce CPU/Memory constraints, increasing training convergence by <b>40%</b>.", bullet_style))
elements.append(Paragraph("&bull; Engineered a <b>Permutation-Invariant Set-Attention Policy</b>, enabling <b>zero-shot generalization</b> to clusters 2x larger than training environments without performance degradation.", bullet_style))
elements.append(Spacer(1, 3))

# MealsApp
meals_data = [
    [Paragraph("<b>MealsApp: AI Meal Prep & Recipe Engine</b> &nbsp;|&nbsp; <i>TypeScript, Gemini 2.5, Google APIs, PWA</i>", job_title_style), Paragraph("Sep 2026", job_meta_style)]
]
t_meals = Table(meals_data, colWidths=[5.5*inch, 2.0*inch])
t_meals.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('BOTTOMPADDING', (0,0), (-1,-1), 0), ('TOPPADDING', (0,0), (-1,-1), 0)]))
elements.append(t_meals)
elements.append(Paragraph("&bull; Built a serverless PWA powered by <b>Gemini 2.5 Flash</b> that dynamically adapts recipes and culinary substitutions against live pantry inventory with a calculated Flavor Match Score.", bullet_style))
elements.append(Paragraph("&bull; Integrated multimodal receipt OCR and barcode lookup via Open Food Facts API (3.2M+ items), auto-generating batch cooking schedules into Google Calendar.", bullet_style))
elements.append(Spacer(1, 3))

# SpMV Benchmark
spmv_data = [
    [Paragraph("<b>High-Performance SpMV Benchmark</b> &nbsp;|&nbsp; <i>C, OpenMP, AVX2 SIMD</i>", job_title_style), Paragraph("Mar 2026 &ndash; May 2026", job_meta_style)]
]
t_spmv = Table(spmv_data, colWidths=[5.5*inch, 2.0*inch])
t_spmv.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('BOTTOMPADDING', (0,0), (-1,-1), 0), ('TOPPADDING', (0,0), (-1,-1), 0)]))
elements.append(t_spmv)
elements.append(Paragraph("&bull; Optimized SpMV kernels in C for CSR/ELLPACK/SELL-C-sigma formats using AVX2 SIMD and FMA, achieving <b>85%+ of theoretical peak memory bandwidth</b>.", bullet_style))
elements.append(Paragraph("&bull; Conducted Roofline Analysis to identify memory-bound bottlenecks and implemented row-sorting (sigma-permutation) to balance SIMD efficiency against irregular graph padding.", bullet_style))
elements.append(Spacer(1, 4))

# Skills
elements.append(Paragraph("Technical Skills", section_style))
elements.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#D1D5DB'), spaceBefore=1, spaceAfter=3))

skills_data = [
    [Paragraph("<b>Languages:</b>", skill_label_style), Paragraph("Java, Python, C, C++, Go, SQL, TypeScript, Scala, Hack, PHP, Bash", skill_val_style)],
    [Paragraph("<b>Systems & Frameworks:</b>", skill_label_style), Paragraph("Kafka, Spark, Spring Boot, Apache Iceberg, Redis, JunoDB, OpenMP, Microservices", skill_val_style)],
    [Paragraph("<b>Cloud & DevOps:</b>", skill_label_style), Paragraph("AWS, Kubernetes, Docker, Jenkins, CI/CD, Terraform, Linux, Maven, Gradle, OpenTelemetry", skill_val_style)],
    [Paragraph("<b>Data & Storage:</b>", skill_label_style), Paragraph("PostgreSQL, MySQL, MongoDB, DynamoDB, Jakarta JPA, Hibernate, Connection Pooling", skill_val_style)]
]
t_skills = Table(skills_data, colWidths=[1.8*inch, 5.7*inch])
t_skills.setStyle(TableStyle([
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('BOTTOMPADDING', (0,0), (-1,-1), 1),
    ('TOPPADDING', (0,0), (-1,-1), 1)
]))
elements.append(t_skills)

doc.build(elements)
print("Resume generated successfully at", pdf_path)
