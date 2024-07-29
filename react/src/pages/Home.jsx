import React from "react";
import "./Home.css";

function Home() {
  return (
    <>
      <div className="homeTitle">
        <h1>Welcome To Home</h1>
      </div>

      <div className="introduction">
        <h2>Introductions to File Management Service:</h2>
        <p className="homeText">
          &emsp;&emsp;Welcome to the File Management Service. This is a file
          management service for users to lookup and manage files. There are two
          main services provided:
        </p>
        <h3>The AccessAPI System</h3>
        <p>
          By using the AccessAPI system, we are able to call directly to the
          file-management-service APIs. Checking the API documentations before
          using is recommanded.&emsp;&emsp;
          <a href="https://github.com/ja166667167/File-Management-Service">
            Github repository and Documentaion
          </a>
        </p>
        <h3>The FileGUI system</h3>
        <p>
          The FileGUI system provides an actual File system GUI for users to
          lookup files
        </p>
      </div>
    </>
  );
}

export default Home;
