import { useNavigate } from "react-router-dom";
import "./apis.css";
import { useState } from "react";
import { listUsers } from "../../services/FileAPIs.js";

function ListUsersApi() {
  const navigate = useNavigate();
  const [listUsersResp, setListUsersResp] = useState("{}");
  async function callAPI() {
    const resp = await listUsers();
    setListUsersResp(resp);
  }
  return (
    <>
      <div>
        <button className="back-button" onClick={() => navigate(-1)}>
          Back
        </button>
      </div>
      <h2>listUsers API</h2>
      <div className="api-content">
        <div className="Inputs">
          <strong>Press to List Users: </strong>
          <span>No input requires:</span>
          <button className="sendButton" onClick={callAPI}>
            List All Users
          </button>
        </div>
        <div className="Outputs">
          <strong>Outputs:&emsp;&emsp;</strong>
          <pre className="APIResponses">{listUsersResp}</pre>
        </div>
      </div>
    </>
  );
}

export default ListUsersApi;
