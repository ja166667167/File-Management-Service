import { BACKEND_HOST, BACKEND_API_KEY } from "../Const.js";

const headers = {
  "Content-Type": "application/json",
  "API-KEY": BACKEND_API_KEY,
};

export async function getRecords(userName) {
  const response = await fetch(`${BACKEND_HOST}files/?username=${userName}`, {
    method: "GET",
    headers: headers,
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error("GetRecords Failed");
      }
      return response.json();
    })
    .then((data) => {
      const jsonString = JSON.stringify(data, null, 4);
      return jsonString;
    })
    .catch((error) => {
      console.log(error);
    });
  return response;
}

export async function listObjects(userName, filePath) {
  const response = await fetch(
    `${BACKEND_HOST}listObj/?username=${userName}&filepath=${filePath}`,
    {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        "API-KEY": BACKEND_API_KEY,
      },
    }
  )
    .then((response) => {
      if (!response.ok) {
        throw new Error("List Objects Failed");
      }
      return response.json();
    })
    .then((data) => {
      const jsonString = JSON.stringify(data, null, 4);
      return jsonString;
    })
    .catch((error) => {
      console.log(error);
    });
  return response;
}

export async function listUsers() {
  const response = await fetch(`${BACKEND_HOST}listUsers/`, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
      "API-KEY": BACKEND_API_KEY,
    },
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error("listUsers Failed");
      }
      return response.json();
    })
    .then((data) => {
      const jsonString = JSON.stringify(data, null, 4);
      return jsonString;
    })
    .catch((error) => {
      console.log(error);
    });
  return response;
}

export async function uploadRecord(postBody) {
  const response = await fetch(`${BACKEND_HOST}files/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "API-KEY": BACKEND_API_KEY,
    },
    body: JSON.stringify(postBody),
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error("Upload record Failed");
      }

      return response.json();
    })
    .then((data) => {
      const jsonString = JSON.stringify(data, null, 4);
      return jsonString;
    })
    .catch((error) => {
      console.log(error);
    });
  return response;
}

export async function deleteRecord(userName, filePath, fileName) {
  const response = await fetch(
    `${BACKEND_HOST}deleteRecord/?username=${userName}&filename=${fileName}&filepath=${filePath}`,
    {
      method: "DELETE",
      headers: {
        // "Content-Type": "application/json",
        "API-KEY": BACKEND_API_KEY,
      },
    }
  )
    .then((response) => {
      if (!response.ok) {
        throw new Error("Deleting record Failed");
      }
      return response.json();
    })
    .then((data) => {
      const jsonString = JSON.stringify(data, null, 4);
      return jsonString;
    })
    .catch((error) => {
      console.log(error);
    });
  return response;
}
