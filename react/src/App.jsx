import { useState } from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import "./App.css";
import Home from "./pages/Home.jsx";
import FileGUI from "./pages/FileGUI.jsx";
import AccessAPI from "./pages/AccessAPI.jsx";
import PageNotFound from "./pages/PageNotFound.jsx";
import Header from "./components/Header/Header.jsx";
import GetRecordsApi from "./pages/AcessAPIs/GetRecordsApi.jsx";
import UploadRecordApi from "./pages/AcessAPIs/UploadRecordApi.jsx";
import ListUsersApi from "./pages/AcessAPIs/ListUsersApi.jsx";
import ListObjectsApi from "./pages/AcessAPIs/ListObjectsApi.jsx";
import DeleteRecordApi from "./pages/AcessAPIs/DeleteRecordApi.jsx";
import UserGUI from "./pages/FileGUI/UserGUI.jsx";

function App() {
  return (
    <BrowserRouter>
      <div className="app">
        <Header />
        <main className="content">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/AccessAPI" element={<AccessAPI />} />
            <Route path="/FileGUI" element={<FileGUI />} />
            <Route path="/GetRecordsApi" element={<GetRecordsApi />} />
            <Route path="/UploadRecordApi" element={<UploadRecordApi />} />
            <Route path="/ListUsersApi" element={<ListUsersApi />} />
            <Route path="/ListObjectsApi" element={<ListObjectsApi />} />
            <Route path="/DeleteRecordApi" element={<DeleteRecordApi />} />
            <Route path="/UserGUI" element={<UserGUI />} />
            <Route path="/*" element={<PageNotFound />} />
          </Routes>
        </main>
      </div>
    </BrowserRouter>
  );
}

export default App;
