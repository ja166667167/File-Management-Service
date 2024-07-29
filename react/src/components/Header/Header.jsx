// Header.js
import React from "react";
import { Link } from "react-router-dom";
import "./Header.css";

function Header() {
  return (
    <header className="header">
      <h1 className="header-title">File Management Service</h1>
      <nav className="nav">
        <ul className="nav-list">
          <li className="nav-item">
            <Link to="/" className="nav-button">
              Home
            </Link>
          </li>
          <li>
            <Link to="/AccessAPI" className="nav-button">
              AccessAPI
            </Link>
          </li>
          <li>
            <Link to="/FileGUI" className="nav-button">
              FileGUI
            </Link>
          </li>
        </ul>
      </nav>
    </header>
  );
}

export default Header;
