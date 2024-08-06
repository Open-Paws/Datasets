# Video Transcripts Dataset

This folder contains data from video transcripts managed by various animal advocacy organizations and individual animal advocates.

## Contents
Each file includes:
- Video URL
- Title
- Youtuber
- Post date
- Time
- Text
- Position

## Data Sharing and Usage Agreement
All data included in this dataset has been shared by participating animal advocacy organizations and individual advocates under data sharing agreements. These agreements permit the inclusion of the data in this database. The data sharing agreements ensure that all data is used ethically and can be freely used in AI and ML applications for animal advocacy.

## Example Data

| Video_URL                                         | Title             | Youtuber         | Post_date  | Time  | Text                                                            | Position |
|---------------------------------------------------|-------------------|------------------|------------|-------|-----------------------------------------------------------------|----------|
| https://www.youtube.com/watch?v=example1          | Example Title 1   | Example Youtuber | 01 Jan 2023 | 0:00  | This is an example transcript text for the first chunk of the video. | 1        |
| https://www.youtube.com/watch?v=example1          | Example Title 1   | Example Youtuber | 01 Jan 2023 | 0:21  | This is an example transcript text for the second chunk of the video. | 2        |
| https://www.youtube.com/watch?v=example1          | Example Title 1   | Example Youtuber | 01 Jan 2023 | 0:43  | This is an example transcript text for the third chunk of the video.  | 3        |
| https://www.youtube.com/watch?v=example2          | Example Title 2   | Example Youtuber | 02 Jan 2023 | 0:00  | This is an example transcript text for the first chunk of the video. | 1        |
| https://www.youtube.com/watch?v=example2          | Example Title 2   | Example Youtuber | 02 Jan 2023 | 0:20  | This is an example transcript text for the second chunk of the video. | 2        |
| https://www.youtube.com/watch?v=example2          | Example Title 2   | Example Youtuber | 02 Jan 2023 | 0:40  | This is an example transcript text for the third chunk of the video.  | 3        |

## Explanation of Position and Time
- **Position**: Each transcript is broken into chunks, and the "Position" indicates the order of these chunks within the video. For example, a position of 1 means that the text is from the first chunk of the video, a position of 2 means it is from the second chunk, and so on. This helps to understand the sequence of the transcript as it appears in the video.
- **Time**: The "Time" indicates the timestamp for the beginning of that section of the transcript within the video. For example, a time of "0:00" means that the text in that chunk starts at the very beginning of the video, "0:21" means it starts at 21 seconds into the video, etc.
