import { Link } from "react-router-dom";
import "./AccessAPI.css";

const RequireApiList = ["GetRecords", "UploadRecord"];
const ExtraApiList = ["ListUsers", "ListObjects", "DeleteRecord"];

function AccessAPI() {
  return (
    <div className="AccessAPI">
      <h3>Required APIs:</h3>
      <ul>
        {RequireApiList.map((api) => (
          <li key={api}>
            <Link to={`/${api}Api`}>{api}</Link>
          </li>
        ))}
      </ul>
      <h3>Additional APIs:</h3>
      <ul>
        {ExtraApiList.map((api) => (
          <li key={api}>
            <Link to={`/${api}Api`}>{api}</Link>
          </li>
        ))}
      </ul>{" "}
    </div>
  );
}

export default AccessAPI;
