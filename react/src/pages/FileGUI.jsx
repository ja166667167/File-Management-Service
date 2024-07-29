import { useNavigate, Link } from "react-router-dom";
import "./FileGUI.css";
import { listUsers } from "../services/FileAPIs";
import { useEffect, useState } from "react";
// import { UserGUI } from "./FileGUI/UserGUI.jsx";
function FileGUI() {
  const navigate = useNavigate();
  const [userList, setUserList] = useState([]);
  const getUserList = async () => {
    try {
      const result = await listUsers();
      // console.log(JSON.parse(result));
      setUserList(JSON.parse(result).users);
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };
  useEffect(() => {
    getUserList();
  }, []);
  // console.log(userList);
  return (
    <>
      <button className="back-button" onClick={() => navigate(-1)}>
        Back
      </button>
      <div className="gui-container">
        <h2>FileGUI</h2>
        <h4>Welcome to the GUI, please select a user to start.</h4>

        <div className="gui-list">
          <ul className="user-list">
            {userList &&
              userList.map((user) => (
                <li key={user}>
                  <Link
                    className="user-link"
                    to="/UserGUI"
                    state={{ user: user, path: "/" }}
                  >
                    {user}
                  </Link>
                </li>
              ))}
          </ul>
        </div>
        <h4 className="no-user-notification">
          If there's no user listed on the right side, please make sure there
          are files in the File Management Service and refresh the page
        </h4>
        <button className="refresh-button" onClick={getUserList}>
          refresh
        </button>
      </div>
    </>
  );
}
export default FileGUI;
