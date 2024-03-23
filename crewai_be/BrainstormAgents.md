This document outlines the structure and functionality of the Company Research Agents class.

The Company Research Agents class is initialized with three main tools: a search internet tool, a YouTube search tool, and a language model. The search internet tool is specifically the SerperDevTool, the YouTube search tool is the YoutubeVideoSearchTool, and the language model is set to use "gpt-4-turbo-preview".

There are two main functions within this class:

1. **Research Manager Function**:
   - This function is designed to manage research tasks for a list of companies and positions.
   - The goal is to generate a list of JSON objects. Each object should contain URLs for three recent blog articles and the URL and title for three recent YouTube interviews for each position in each company.
   - The requirements include ensuring the final list covers all companies and positions, filling missing information with "MISSING", not generating fake information, and not stopping the research until all requested information is found.
   - The backstory provided explains that the role of the Company Research Manager is to aggregate all the researched information into a list.
   - The function utilizes the language model and both search tools, operates in verbose mode, and allows delegation.

2. **Company Research Agent Function**:
   - This function focuses on looking up specific positions for a given company and finding URLs for three recent blog articles and the URL and title for three recent YouTube interviews for each position.
   - The goal is to return this collected information in a JSON object format.
   - The important points include stopping the search once the information is found, returning only the requested information, ensuring the person's name who holds the position is found, and not generating fake information.
   - The backstory provided describes the role of the Company Research Agent as responsible for looking up specific positions within a company and gathering relevant information.
   - This function also utilizes the language model and both search tools and operates in verbose mode.

