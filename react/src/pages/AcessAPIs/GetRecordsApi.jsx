import { useNavigate } from "react-router-dom";
import "./apis.css";
import { useState } from "react";
import { getRecords } from "../../services/FileAPIs.js";

function GetRecordsApi() {
  const navigate = useNavigate();
  const [getRecordsResponse, setGetRecordsResponse] = useState("{}");
  async function callAPI() {
    const userName = document.getElementById("userName").value;
    const resp = await getRecords(userName);
    setGetRecordsResponse(resp);
  }
  return (
    <>
      <div>
        <button className="back-button" onClick={() => navigate(-1)}>
          Back
        </button>
        <h2>GetRecords API</h2>
      </div>
      <div className="api-content">
        <div className="Inputs">
          <strong>Inputs:&emsp;&emsp;</strong>
          <div className="input-list">
            <span>userName:&emsp;&emsp;</span>
            <input type="text" id="userName"></input>
          </div>

          <button className="sendButton" onClick={callAPI}>
            Get Records
          </button>
        </div>
        <div className="Outputs">
          <strong>Outputs:&emsp;&emsp;</strong>
          <pre className="APIResponses">{getRecordsResponse}</pre>
        </div>
      </div>
    </>
  );
}

export default GetRecordsApi;
