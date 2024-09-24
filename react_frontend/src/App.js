import React, { useState } from "react";
import axios from "axios";
import "./styles.css";

function App() {
  const [videoId, setVideoId] = useState("");
  const [videoData, setVideoData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleFetchData = async () => {
    setLoading(true);
    setError(null);
    try {
      const response = await axios.get(`http://localhost:8000/api/video/`, {
        params: { video_id: videoId },
      });
      setVideoData(response.data);
    } catch (err) {
      setError("Failed to fetch video data. Please check the video ID.");
    }
    setLoading(false);
  };

  return (
    <div className="container">
      <h1>
        YouTube Video Data Fetcher <br /> by <br /> {"Odara Rapheal"}
      </h1>

      <input
        type="text"
        value={videoId}
        onChange={(e) => setVideoId(e.target.value)}
        placeholder="Enter YouTube Video ID"
      />
      <button onClick={handleFetchData}>Fetch Video Data</button>

      {loading && <p className="loading">Loading...</p>}
      {error && <p className="error">{error}</p>}

      {videoData && (
        <div>
          <div className="video-details">
            <h2>{videoData.video_details.title}</h2>
            <p>{videoData.video_details.description}</p>
            <p>Views: {videoData.video_details.view_count}</p>
            <p>Likes: {videoData.video_details.like_count}</p>
          </div>
          <div className="comments-section">
            <h3>Comments</h3>
            <ul>
              {videoData.comments.map((comment, index) => (
                <li key={index}>{comment}</li>
              ))}
            </ul>
          </div>
        </div>
      )}
    </div>
  );
}

export default App;
