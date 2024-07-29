import { useNavigate } from "react-router-dom";
import "./apis.css";
import { useState } from "react";
import { BACKEND_HOST, BACKEND_API_KEY } from "../../Const.js";
import { deleteRecord } from "../../services/FileAPIs.js";

function DeleteRecordApi() {
  const navigate = useNavigate();
  const [delResp, setdelResp] = useState("{}");
  async function callAPI() {
    const userName = document.getElementById("userName").value;
    const filePath = document.getElementById("filePath").value;
    const fileName = document.getElementById("fileName").value;
    const rsp = await deleteRecord(userName, filePath, fileName);
    setdelResp(rsp);
  }
  return (
    <>
      <div>
        <button className="back-button" onClick={() => navigate(-1)}>
          Back
        </button>
        <h2>deleteRecord API</h2>
      </div>
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
            Delete
          </button>
        </div>
        <div className="Outputs">
          <strong>Outputs:&emsp;&emsp;</strong>
          <pre className="APIResponses">{delResp}</pre>
        </div>
      </div>
    </>
  );
}

export default DeleteRecordApi;
