import { useNavigate } from "react-router-dom";
import "./apis.css";
import { useState } from "react";
import { BACKEND_HOST, BACKEND_API_KEY } from "../../Const.js";
import { uploadRecord } from "../../services/FileAPIs.js";

function UploadRecordApi() {
  const navigate = useNavigate();
  const [postResp, setPostResp] = useState("{}");
  async function callAPI() {
    const postBody = {
      user_name: document.getElementById("userName").value,
      file_path: document.getElementById("filePath").value,
      file_name: document.getElementById("fileName").value,
    };
    const rsp = await uploadRecord(postBody);
    setPostResp(rsp);
  }
  return (
    <>
      <div>
        <button className="back-button" onClick={() => navigate(-1)}>
          Back
        </button>
      </div>
      <h2>UploadRecords API</h2>
      <div className="api-content">
        <div className="Inputs">
          <strong>Inputs:&emsp;&emsp;</strong>
          <div className="input-list">
            <span>userName:&emsp;&emsp;</span>
            <input type="text" id="userName"></input>
          </div>
          <div className="input-list">
            <span>filePath:&emsp;&emsp;</span>
            <input type="text" id="filePath"></input>
          </div>
          <div className="input-list">
            <span>fileName:&emsp;&emsp;</span>
            <input type="text" id="fileName"></input>
          </div>
          <button className="sendButton" onClick={callAPI}>
            Upload
          </button>
        </div>
        <div className="Outputs">
          <strong>Outputs:&emsp;&emsp;</strong>
          <pre className="APIResponses">{postResp}</pre>
        </div>
      </div>
    </>
  );
}

export default UploadRecordApi;
