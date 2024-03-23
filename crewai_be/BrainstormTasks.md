### Company Research Tasks Class

#### Initialization
- Initializes with a `job_id`.

#### Append Event Callback
- Logs the callback invocation with the task output.
- Appends the event with the job ID and the exported task output.

#### Manage Research Method
- **Description**: 
  - Based on a list of companies and positions, utilizes the results from the Company Research Agent to research each position in each company.
  - Gathers information using web search and YouTube, aiming to find 3 blog articles and 3 YouTube interviews for each position within each company, including metadata such as URLs and titles.
- **Agent**: The agent responsible for executing the task.
- **Expected Output**: A JSON object detailing the company name, position name, blogs, and YouTube interviews with their titles and URLs.
- **Callback**: Calls the append event callback upon task completion.
- **Context**: The tasks context.
- **Output JSON**: PositionInfoList, a structured format for the output.

#### Company Research Method
- **Description**: 
  - Researches positions for a specific company.
  - For each position, finds 3 recent blog articles and 3 recent YouTube interviews, including their URLs and titles.
  - Compiles this information into a JSON object.
  - Provides helpful tips for locating blog articles and YouTube interviews, emphasizing the importance of genuine information and persistence in research.
- **Agent**: The agent assigned to carry out the research task.
- **Expected Output**: A JSON object containing the company name, positions, blogs, and YouTube interviews with titles and URLs.
- **Callback**: Invokes the append event callback upon task completion.
- **Output JSON**: PositionInfo, a structured format for the output.
- **Async Execution**: Indicates that the task is executed asynchronously.

