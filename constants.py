skill_col_size = 5

#publication_url --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
linkedin_logo = '''                                                                                                                                          
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
  <i class="fa-brands fa-linkedin" style="font-size: 28px;"></i>                                                                           
'''

github_logo = '''
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
  <i class="fa-brands fa-github" style="font-size: 28px;"></i>                                                                           
'''
header_home_en = ["About Me", "My Skills", "Who Am I?"]
header_home_fr = ["À propros de moi","Mes Compétences","Qui suis-je?"]
# personal info (for main page) --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
info_en = {'brief':
              """
                Graduated from a Telecommunication and Informatics Engineering in 2019 and I've since been developing my career towards Systems/Applications and Infrastructure.
                I love to work at this level as I feel it rewards me with a holistic comprehensive view of the whole "puzzle".
                I am passionate and curious about technology and exploring new ways of applying my knowledge to real life problems and business settings.
                I'm also learning and trying to develop data analysis skills.
                Curious, rational and analytical at core. 
              """,
        'name':'Rodrigo Rocha',
        'description':'I\'m a telecommunication engineer that had been working with systems and infrastructure with a passion for technology.', 
        'study':'Instituto Superior Técnico - University of Lisbon',
        'location':'Toulouse, France',
        'interest':'Systems/Infrastructure Engineering, Product Management, Data Analysis, Finance, Economy, Business',
        'skills':['Linux','Windows','Apache','Confluence','JIRA','ServiceNow','Git','Github','Gitlab CI','Control M','PostgreSQL','Nagios','Grafana','ELK','Excel','JS7 Job Scheduler','Notion','Syslog','Sharepoint','Wireshark','MySQL','Azure DevOps','REST API','Docker','Kubernetes','Streamlit','Pandas','Shell','PowerShell','Python','XML','JSON','Matlab','Postman','Amazon S3','SCRUM','TCP/IP stack'],
        'WAI':
              """
              I'm Rodrigo, a Telecommunication and Informatics Engineer from Lisbon, Portugal. 
              As an Engineer, I bring attention to detail, and problem-solving skills to every project I undertake. I thrive in environments that challenge me to think and find solutions.
              
              Outside of work, I'm developing myself in different axis, being learning about investments, learning to play piano or training and dieting.  
              These passions not only enrich my personal life but also contribute to my general health contributing to my professional endeavors.
              
              I hope that with this webpage, I can show and leverage some of my technical skills by building small projects in order to exercise some skills that I haven't acquired or I'm still in the process of acquiring.

              Feel free to check all of the info that is present on this website. And if anything sounds interesting to you, please consider to contact me though the Contact section.
            """
        }

info_fr = {'brief':
            """
            Diplômé en Ingénierie des Télécommunications et de l'Informatique en 2019, j'ai orienté ma carrière vers les Systèmes/Applications et l'Infrastructure.
            J'adore travailler à ce niveau car je sens que cela me récompense avec une vision holistique et globale de tout le "puzzle".
            Je suis passionné et curieux de la technologie et j'explore de nouvelles façons d'appliquer mes connaissances à des problèmes réels et à des environnements professionnels.
            Je suis également en train d'apprendre et de développer des compétences en analyse de données.
            Curieux, rationnel et analytique surtout.  
            """,
        'name':'Rodrigo Rocha',
        'description':'Je suis un ingénieur de télécommunication qui aime travailler sur des systèmes et infrastructures et a une passion pour la technologie.', 
        'study':'Instituto Superior Técnico - Université de Lisbonne',
        'location':'Toulouse, France',
        'interest':'Ingénierie Systèmes/Infrastructure, Gestion de Produit, Analyse de Données, Finance, Économie, Business',
        'skills':['Linux','Windows','Apache','Confluence','JIRA','ServiceNow','Git','Github','Gitlab CI','Control M','PostgreSQL','Nagios','Grafana','ELK','Excel','JS7 Job Scheduler','Notion','Syslog','Sharepoint','Wireshark','MySQL','Azure DevOps','REST API','Docker','Kubernetes','Streamlit','Pandas','Shell','PowerShell','Python','XML','JSON','Matlab','Postman','Amazon S3','SCRUM','TCP/IP stack'],
        'WAI':
              """
              Je m'appelle Rodrigo, je suis un ingénieur en télécommunications et informatique de Lisbonne, Portugal.
              En tant qu'ingénieur, j'apporte un attention aux détails et des compétences en résolution de problèmes à chaque projet que j'entreprends. Je m'épanouis dans des environnements qui me mettent au défi de réfléchir et de trouver des solutions.
              
              Dehors du travail, je me développe dans différents axes, je me renseigne sur les investissements, j'apprends à jouer du piano et je m'entraîne à la salle du sport.
              Ces passions enrichissent non seulement ma vie personnelle mais contribuent également à ma santé générale en contribuant à mes efforts professionnels.
              
              J'espère qu'avec cette page Web, je pourrai montrer et mettre à profit certaines de mes compétences techniques en construisant de petits projets afin d'exercer certaines compétences que je n'ai pas acquises ou que je suis encore en train d'acquérir.

              N'hésitez pas à consulter toutes les informations présentes sur ce site. Et si quelque chose vous intéresse, pensez à me contacter via la section Contact.
            """
        }
# Experience --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

headers_resume_en=["TODO_EN","Hard Skills","Work History"]
headers_resume_fr=["TODO_FR","Compétences Techniques","Expérience Professionnelle"]




#[[header, subheader, date, location, content, link, link_url], [...], etc.]

Experience = [
              [":blue[Zbyte] Technology | Data Warehouse Startup", "Product Manager Intern", 
              "May 2023 – Sep 2023", "Hangzhou, China", 
              """
              - Designed a **LLM - Dataset** chat app’s architecture with PM director, in which user could upload private datasets enabling LLM chat app response more accurately to domain-specific inquiries.
              - Maintained and fixed 150+ detailed errors in reusable **React** components for a web-base Data Warehouse while communicate with UI designers for ”designer review”.
              - Drafted and perfected the documentation for a Data Warehouse, including Data Types, 50+ SQL Commands, and 10+ Build-in Functions.
              - Published 3 articles, each attracts 5k+ reads for the company‘s tech blog; including two Analysis of Forrester and G2’s review on Cloud Data Warehouse.
              """,
              "Company website", "https://relyt.cloud"],

              [":violet[Branda] | Brandeis Campus App", "Software Engineer", 
                "Jan 2023 – present", "Waltham, MA", 
                """
                - Collaborated in a **Agile** software development cycle, main responsible for improving the mobile UI/UX.
                - Implemented a interactive calendar daily used by 1.6K student to keep track of school events, using **REST APIs** with **React Native** as the front-end. Utilized **Redis** to cache hotspot data, reducing the workload on main database.
                - Managed database migration from Heroku to **Firebase** to meet user growth, implemented API touchpoints within the CI/CD pipeline for migration testing.
                """,
                "App Store link", "https://apps.apple.com/us/app/branda/id1437022581"],

              ["Brandeis :orange[Quant Club]", "Software Engineer", 
                "Jan 2023 – Sep 2023", "Waltham, MA", 
                """
                - Contribute to research, gather, and analyze information of different companies where we show users companies’ volatility indices using Python.
                - Designed and developed a website that allows users to see data regarding companies’ volatility indices utilizing **JavaScript, React, and Node.js** (setting up the website’s skeleton, capable of automatically giving users the most up-to-date information).
                """,
              "Club website", "https://brandeisquantclub.org"],

              [":orange[Brandeis University] | Anthropology Department", "Research Assistant",
                "Sep 2022 – Aug 2023", "Waltham, MA", 
                """
                - Collaborated with Anthropology professor Elizabeth Ferry on researching asset tokenization and cryptocurrencies as cultural phenomena.
                - Interviewed 17 people who worked in Finance and IT industry during the summer; asking about their opinion on Gold Tokenization, Bitcoin, Blockchain, and Central Bank digital Currency in China. These finding support and enrich Professor Ferry’s ongoing book writing about Gold in mining and finance.
                - Weekly report based on searching for and reading news, social media reports, and journalistic and academic analyses.
                """,
                "Department website", "https://www.brandeis.edu/anthropology/undergraduate/research-and-funding/student-bios.html"]
              ]      

# Portfolio --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#     {'project1':[HEADER, CONTENT]
#      'project2':[HEADER, CONTENT]
#      ...}

Portfolio = { 1:[':blue[Deis]Evaluation - Course Evaluation Website',
              """
              Launched a course evaluation web app for Brandeis students to review and share courses, exceeding 200+ active users.
              Designed the whole UI with Figma and Implemented front end with Javascript, HTML/CSS in a MERN Stack.
              """],
              2:['Data Visualization in :orange[D3.js]',
                  """
                Created a data visualization web app for Massachusetts police expenditure data using D3.js.
                """],
              3:[':blue[LLM] Desktop ChatApp',
                """
                - Designed and developed a cross-platform **desktop LLM Chat app**, enabling chat over user-upload dataset; providing a more accurate response to domain-specific inquiries than ChatGPT.
                - Utilized Embedding and Searching from **OpenAI API** to optimize Chat app’s response. Split the user-upload file into small chunks; used OpenAI Embedding model to vectorize each chunk and save them into Qdrant database. Transform user query to vector using OpenAI, and then inquire the top match text chunk from Qdrant database using topk value.
                """],
              4:[':orange[Anthropology] Research Project - A Timeless Building',
                """
                - An **qualitative anthropological research** on the preservation and adaption of historical sites; as final project, received the highest score in class.
                - My fieldwork includes interviewing educators, examing archive, on-site obervation. Through my fieldwork at King’s Chapel, I argued for a humane approach to preserving historic sites, that seeks a balance between **maintaining the historical significance and the sites’ adaptations to societal changes**.
                """]
            }
              
# Contacts --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

header_contact_en = ["Get In Touch With Me!","Other Links"]
header_contact_fr = ["Contactez moi!","Autres liens"]
phone = "(+351) 93 258 23 18"
email = "rodrigo.rocha582@gmail.com"
linkedin_link = "www.linkedin.com/in/rodrigo-rocha"
github_link = "https://github.com/morrison93"


# iframes --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
figma_iframe = '<iframe style="border: 1px solid rgba(0, 0, 0, 0.1);" width="800" height="450" src="https://www.figma.com/embed?embed_host=share&url=https%3A%2F%2Fwww.figma.com%2Ffile%2FlMYyNOptCmZb5JlYXmKkif%2FCourseEvaluation%3Ftype%3Ddesign%26node-id%3D160%253A1249%26mode%3Ddesign%26t%3DEj6BVdYEZCLgxthB-1" allowfullscreen></iframe>'

figma_link = "https://www.figma.com/embed?embed_host=share&url=https%3A%2F%2Fwww.figma.com%2Ffile%2FlMYyNOptCmZb5JlYXmKkif%2FCourseEvaluation%3Ftype%3Ddesign%26node-id%3D160%253A1249%26mode%3Ddesign%26t%3DEj6BVdYEZCLgxthB-1"

StoryMap_iframe = "https://storymaps.arcgis.com/stories/dfb9689618e343cf9f6ef36d9a8329a7?header"

Evaluation_html = '''
                <div class="github-card" data-github="Rsirp0c/deis-course-evaluation" data-width="400" data-height="" data-theme="default"></div>
                <script src="https://cdn.jsdelivr.net/github-cards/latest/widget.js"></script>                
                '''