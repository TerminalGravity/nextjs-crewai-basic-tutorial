This is a [Next.js] app for interfacing with a flask server .... crewai ... python ... 



## Getting Started

First, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

The frontend of this Next.js application is designed to interact with a Flask backend to automate market research tasks. It allows users to input companies and positions they're interested in researching, then communicates with the backend to fetch and display relevant data, such as blog articles and YouTube videos.

### How the Frontend Works:

1. **Input Section**: Users can input companies and positions they want to research. This is handled by the [InputSection](file:///Users/<>/Repos/nextjs-crewai-basic-tutorial/nextjs_app/app/page.tsx#5%2C8-5%2C8) component, which collects user inputs and updates the state accordingly.

2. **Starting the Job**: Once the inputs are provided, users can start the research job by clicking the "Start" button. This triggers a request to the Flask backend to initiate the research task.

3. **Displaying Results**: The application continually checks for updates from the backend and displays the results in the [FinalOutput](file:///Users/<>/Repos/nextjs-crewai-basic-tutorial/nextjs_app/app/page.tsx#4%2C10-4%2C10) and [EventLog](file:///Users/<>/Repos/nextjs-crewai-basic-tutorial/nextjs_app/app/page.tsx#3%2C10-3%2C10) components. The [FinalOutput](file:///Users/<>/Repos/nextjs-crewai-basic-tutorial/nextjs_app/app/page.tsx#4%2C10-4%2C10) shows the main findings, while [EventLog](file:///Users/<>/Repos/nextjs-crewai-basic-tutorial/nextjs_app/app/page.tsx#3%2C10-3%2C10) provides a log of events or updates from the backend.

4. **State Management**: The [useCrewJob](file:///Users/<>/Repos/nextjs-crewai-basic-tutorial/nextjs_app/app/page.tsx#6%2C10-6%2C10) hook manages the state of the application, including the list of companies, positions, and the status of the research job. This hook centralizes the logic for interacting with the backend and updating the UI based on the job's progress.

### Making Changes to Components or Structure:

To modify the frontend or its components, consider the following steps:

- **Update UI Components**: Modify existing components like [InputSection](file:///Users/<>/Repos/nextjs-crewai-basic-tutorial/nextjs_app/app/page.tsx#5%2C8-5%2C8), [FinalOutput](file:///Users/<>/Repos/nextjs-crewai-basic-tutorial/nextjs_app/app/page.tsx#4%2C10-4%2C10), or [EventLog](file:///Users/<>/Repos/nextjs-crewai-basic-tutorial/nextjs_app/app/page.tsx#3%2C10-3%2C10) to change how information is displayed. For instance, to change the layout of the input section, you would edit `InputSection.tsx`.

- **Add New Features**: Introduce new components and integrate them with the existing state management logic. For example, adding a new feature to filter results could involve creating a new component and updating the [useCrewJob](file:///Users/<>/Repos/nextjs-crewai-basic-tutorial/nextjs_app/app/page.tsx#6%2C10-6%2C10) hook to handle the filtering logic.

- **Enhance Interactivity**: Improve user interaction by adding features like real-time validation of inputs or visual feedback during the research job. This might involve updating components to include new event handlers and state updates.

- **Refactor for Performance**: Optimize the application by refactoring components or hooks for better performance. This could include memoizing components to prevent unnecessary re-renders or optimizing state updates in the [useCrewJob](file:///Users/<>/Repos/nextjs-crewai-basic-tutorial/nextjs_app/app/page.tsx#6%2C10-6%2C10) hook.

### Example: Adding a New Feature

Suppose you want to add a feature to cancel an ongoing research job. You would:

1. **Update the [useCrewJob](file:///Users/<>/Repos/nextjs-crewai-basic-tutorial/nextjs_app/app/page.tsx#6%2C10-6%2C10) Hook**: Add a method to send a cancellation request to the backend.

2. **Modify the UI**: Add a "Cancel" button to the interface, perhaps next to the "Start" button in [page.tsx](file:///Users/<>/Repos/nextjs-crewai-basic-tutorial/nextjs_app/app/page.tsx#1%2C1-1%2C1), and tie its [onClick](file:///Users/<>/Repos/nextjs-crewai-basic-tutorial/nextjs_app/app/page.tsx#33%2C15-33%2C15) event to the cancellation method in [useCrewJob](file:///Users/<>/Repos/nextjs-crewai-basic-tutorial/nextjs_app/app/page.tsx#6%2C10-6%2C10).

```typescript:nextjs_app/app/page.tsx
// Inside the return statement, add a Cancel button
<button
  onClick={() => crewJob.cancelJob()}
  className="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded text-sm"
  disabled={!crewJob.running}
>
  Cancel
</button>
```

3. **Handle Backend Communication**: Ensure the Flask backend can handle the cancellation request and terminate the job appropriately.

This approach keeps changes modular and focused, allowing for incremental improvements and feature additions to the frontend interface.

The frontend of this Next.js application is structured to facilitate user interaction for submitting research jobs and displaying the results. The backend, built with Flask, handles these requests, performs the research, and sends back updates and results.

### Frontend Workflow:

1. **User Input**: Through the [InputSection](file:///Users/jackfelke/Repos/nextjs-crewai-basic-tutorial/nextjs_app/app/page.tsx#5%2C8-5%2C8) component, users input companies and positions they're interested in researching. This component updates the application's state with the user's input.

2. **Starting Research**: The "Start" button triggers the [startJob](file:///Users/jackfelke/Repos/nextjs-crewai-basic-tutorial/nextjs_app/app/page.tsx#33%2C38-33%2C38) function from the [useCrewJob](file:///Users/jackfelke/Repos/nextjs-crewai-basic-tutorial/nextjs_app/app/page.tsx#6%2C10-6%2C10) hook, which sends a request to the Flask backend to initiate the research job.

3. **Displaying Results**: The frontend periodically polls the backend for updates using the [fetchJobStatus](file:///Users/jackfelke/Repos/nextjs-crewai-basic-tutorial/nextjs_app/hooks/useCrewJob.tsx#39%2C11-39%2C11) function within the [useCrewJob](file:///Users/jackfelke/Repos/nextjs-crewai-basic-tutorial/nextjs_app/app/page.tsx#6%2C10-6%2C10) hook. Results are displayed in the [FinalOutput](file:///Users/jackfelke/Repos/nextjs-crewai-basic-tutorial/nextjs_app/app/page.tsx#4%2C10-4%2C10) component, and updates are logged in the [EventLog](file:///Users/jackfelke/Repos/nextjs-crewai-basic-tutorial/nextjs_app/app/page.tsx#3%2C10-3%2C10) component.

4. **State Management**: The [useCrewJob](file:///Users/jackfelke/Repos/nextjs-crewai-basic-tutorial/nextjs_app/app/page.tsx#6%2C10-6%2C10) hook centralizes the state and logic for managing research jobs, including starting jobs, polling for updates, and storing results.

### Backend Communication:

1. **Starting a Job**: The frontend sends a POST request to start a job, including the companies and positions as payload. The backend initiates the research and returns a job ID for tracking.

    
```88:95:nextjs_app/hooks/useCrewJob.tsx
  const startJob = async () => {
    // Clear previous job data
    setEvents([]);
    setPositionInfoList([]);
    setRunning(true);

    try {
      const response = await axios.post<{ job_id: string }>(
```


2. **Polling for Updates**: The frontend periodically sends GET requests using the job ID to check the job's status and fetch any available results or updates.

    
```39:46:nextjs_app/hooks/useCrewJob.tsx
    const fetchJobStatus = async () => {
      try {
        console.log("calling fetchJobStatus");
        const response = await axios.get<{
          status: string;
          result: { positions: PositionInfo[] };
          events: EventType[];
        }>(`http://localhost:3001/api/crew/${currentJobId}`);
```


3. **Handling Responses**: The backend processes these requests, performing the necessary research tasks. It updates the job's status and results, which are then sent back to the frontend in response to the polling requests.

### Enhancing Communication:


For the described Next.js and Flask application, implementing Server-Sent Events (SSE) offers the path of least resistance for enhancing communication between the frontend and backend. SSE is simpler to set up for server-to-client communication, which aligns with the application's need to push updates from the backend to the frontend as research jobs progress.

### Implementing SSE:

#### Backend (Flask):
1. **Create an SSE Endpoint**: Define a Flask route that streams data. Use a generator function to yield data in a format suitable for SSE.

```python
from flask import Flask, Response

app = Flask(__name__)

def stream_data():
    # Example generator function
    # Replace with actual logic to yield data
    yield "data: {}\n\n".format("Server update")

@app.route('/stream')
def stream():
    return Response(stream_data(), content_type='text/event-stream')
```

#### Frontend (Next.js):
1. **Connect to SSE Endpoint**: Use the `EventSource` API to listen for messages from the server.

```typescript:nextjs_app/hooks/useCrewJob.tsx
import { useEffect } from "react";

export const useCrewJob = () => {
  useEffect(() => {
    const eventSource = new EventSource("http://localhost:3001/stream");

    eventSource.onmessage = function(event) {
      console.log("New message from server", event.data);
      // Handle the event data
    };

    return () => {
      eventSource.close();
    };
  }, []);

  // Rest of the hook logic
};
```

This setup allows the Flask backend to send real-time updates to the Next.js frontend without the frontend needing to poll the server. SSE is well-suited for this application's requirements, providing a straightforward and efficient method to push backend updates to the frontend.