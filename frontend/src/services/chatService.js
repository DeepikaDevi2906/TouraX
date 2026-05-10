// frontend/src/services/chatService.js

import API from "./api";


export const sendMessage =
    async (message) => {

    const response = await API.post(

        "/chat",

        {
            message
        }
    );

    return response.data;
};


export const getMessages =
    async () => {

    const response =
        await API.get("/messages");

    return response.data;
};