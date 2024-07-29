import { useState, useEffect } from "react";
import { useNavigate, Link, useLocation } from "react-router-dom";
import { listObjects } from "../../services/FileAPIs";
import "./gui.css";

function UserGUI() {
  const navigate = useNavigate();
  const location = useLocation();
  const currentUser = location.state?.user;
  const currentPath = location.state?.path;
  const [folders, setFolders] = useState();
  const [files, setFiles] = useState();
  const getObj = async () => {
    try {
      const result = await listObjects(currentUser, currentPath);
      // console.log(JSON.parse(result));
      setFolders(JSON.parse(result).folders);
      setFiles(JSON.parse(result).files);
      console.log(JSON.parse(result));
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };
  useEffect(() => {
    getObj();
  }, [currentPath]);
  return (
    <>
      <button className="back-button" onClick={() => navigate(-1)}>
        Back to User list
      </button>

      <h1>{currentUser}</h1>
      <h2>Current File Path: {currentPath}</h2>
      <Link
        className="path-back-button"
        to="/UserGUI"
        state={{
          user: currentUser,
          path:
            currentPath == "/"
              ? currentPath
              : currentPath.replace(/\/[^\/]+\/?$/, "") + "/",
        }}
      >
        File path back one level
      </Link>
      <div>
        <h3>Folders:</h3>
        <ul className="folder-list">
          {folders &&
            folders[0] != "" &&
            folders.map((folder) => (
              <li key={folder}>
                <Link
                  to="/UserGUI"
                  state={{
                    user: currentUser,
                    path: currentPath.slice(0, -1) + folder,
                  }}
                >
                  {folder}
                </Link>
              </li>
            ))}
        </ul>
        <h3>Files:</h3>
        <ul className="file-list">
          {files && files[0] != "" && files.map((file) => <li>{file}</li>)}
        </ul>
      </div>
      {}
    </>
  );
}

export default UserGUI;
