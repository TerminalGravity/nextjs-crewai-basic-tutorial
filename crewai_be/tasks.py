from crewai import Task, Agent
from textwrap import dedent


from job_manager import append_event
from models import PositionInfo, PositionInfoList
from utils.logging import logger


class CompanyResearchTasks():

    def __init__(self, job_id):
        self.job_id = job_id

    def append_event_callback(self, task_output):
        logger.info("Callback called: %s", task_output)
        append_event(self.job_id, task_output.exported_output)

    def manage_research(self, agent: Agent, companies: list[str], positions: list[str], tasks: list[Task]):
        return Task(
            description=dedent(f"""
Based on the list of companies {companies} and the positions {positions}, use the results from the Company Research Agent to research each position in each company.
Utilize web search and YouTube to gather information on each position within each company: 3 blog articles, 3 YouTube interviews - ensure to include metadata such as the URLs and titles.
                """),
            agent=agent,
            expected_output=dedent("""
                {
                    "companyName": {
                        "positionName": {
                            "blogs": [
                                {"title": "Blog Article 1 Title", "url": "http://exampleblog1.com"},
                                {"title": "Blog Article 2 Title", "url": "http://exampleblog2.com"},
                                {"title": "Blog Article 3 Title", "url": "http://exampleblog3.com"}
                            ],
                            "youtubeInterviews": [
                                {"title": "YouTube Interview 1 Title", "url": "http://exampleyoutube1.com"},
                                {"title": "YouTube Interview 2 Title", "url": "http://exampleyoutube2.com"},
                                {"title": "YouTube Interview 3 Title", "url": "http://exampleyoutube3.com"}
                            ]
                        }
                    }
                }
                """),
            callback=self.append_event_callback,
            context=tasks,
            output_json=PositionInfoList
        )

    def company_research(self, agent: Agent, company: str, positions: list[str]):
        return Task(
            description=dedent(f"""Research the positions {positions} for the company {company}. 
                For each position, find 3 recent blog articles and 3 recent YouTube interviews, including their URLs and titles.
                Compile this information into a JSON object.
                               
                Helpful Tips:
                - To locate the blog articles and their URLs, conduct Google searches with queries like:
                    - "{company} [POSITION] blog articles"
                - To find YouTube interviews, search on YouTube with queries like:
                    - "{company} [POSITION] interview"
                               
                Important:
                - Cease searching once you have gathered the requested information.
                - Return only the requested information. NOTHING ELSE!
                - Ensure all information is genuine and refrain from fabricating data.
                - Persist in your research until you have obtained the requested information for each position at the company.
                """),
            agent=agent,
            expected_output=dedent("""
                {
                    "company": "<company_name>",
                    "positions": [
                        {
                            "position": "<position_name>",
                            "blogs": [
                                {"title": "<Blog Article 1 Title>", "url": "<http://exampleblog1.com>"},
                                {"title": "<Blog Article 2 Title>", "url": "<http://exampleblog2.com>"},
                                {"title": "<Blog Article 3 Title>", "url": "<http://exampleblog3.com>"}
                            ],
                            "youtubeInterviews": [
                                {"title": "<YouTube Interview 1 Title>", "url": "<http://exampleyoutube1.com>"},
                                {"title": "<YouTube Interview 2 Title>", "url": "<http://exampleyoutube2.com>"},
                                {"title": "<YouTube Interview 3 Title>", "url": "<http://exampleyoutube3.com>"}
                            ]
                        }
                    ]
                }
                """),
            callback=self.append_event_callback,
            output_json=PositionInfo,
            async_execution=True
        )
