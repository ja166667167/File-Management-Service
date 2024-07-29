import { useNavigate } from "react-router-dom";
import "./apis.css";
import { useState } from "react";
import { listObjects } from "../../services/FileAPIs.js";

function ListObjectsApi() {
  const navigate = useNavigate();
  const [listObjResp, setListObjResp] = useState("{}");

  async function callAPI() {
    const userName = document.getElementById("userName").value;
    const filePath = document.getElementById("filePath").value;
    const resp = await listObjects(userName, filePath);
    setListObjResp(resp);
  }
  return (
    <>
      <div>
        <button className="back-button" onClick={() => navigate(-1)}>
          Back
        </button>
        <h2>ListObj API</h2>
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
          <button className="sendButton" onClick={callAPI}>
            List Objects
          </button>
        </div>
        <div className="Outputs">
          <strong>Outputs:&emsp;&emsp;</strong>
          <pre className="APIResponses">{listObjResp}</pre>
        </div>
      </div>
    </>
  );
}

export default ListObjectsApi;
