"use client";

We start by importing necessary modules and hooks from React and other libraries. This includes axios for making HTTP requests, useEffect and useState from React for managing component lifecycle and state, and toast from react-hot-toast for displaying notifications.

We define three types to structure our data: EventType, NamedUrl, and PositionInfo. Each type outlines the structure of the data we expect to work with. EventType represents an event with a data string and a timestamp. NamedUrl represents a URL with a name and the URL itself. PositionInfo represents detailed information about a position, including the company name, position title, the name of the individual, a list of blog article URLs, and a list of YouTube interview URLs with their names.

We then define a custom hook named useCrewJob. This hook is responsible for managing the state and interactions related to fetching job information and status updates.

Inside the useCrewJob hook, we initialize several pieces of state using the useState hook. This includes:
- running: a boolean indicating if a job is currently running.
- companies: an array of strings representing company names.
- positions: an array of strings representing position titles.
- events: an array of EventType objects representing events that have occurred.
- positionInfoList: an array of PositionInfo objects representing detailed information about positions.
- currentJobId: a string representing the ID of the current job.
- startTime: a Date object or null representing when the current job started.
- endTime: a Date object or null representing when the current job ended.

We use the useEffect hook to perform side effects. Specifically, we set up an interval that periodically fetches the job status if there is a currentJobId. Inside this interval, we make an HTTP GET request to a specific URL with the currentJobId. We then update our state based on the response, including setting the events, positionInfoList, and updating the running state based on the job status. If the job is complete or an error occurs, we clear the interval, set the running state to false, and display a notification.

We define a function named startJob. This function is responsible for starting a new job. It clears any existing job data, sets the running state to true, and records the start time. It then makes an HTTP POST request to start a new job with the selected companies and positions. Upon success, it updates the currentJobId with the job ID from the response and displays a notification. If the request fails, it displays an error notification and resets the currentJobId.

Finally, the hook returns an object containing the state variables and functions, allowing components that use this hook to access and manipulate the job's state and trigger actions like starting a job.

