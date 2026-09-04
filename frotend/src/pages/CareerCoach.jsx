import React from "react";
import "./CareerCoach.css";
import { useParams } from "react-router-dom";
import { useState , useEffect } from "react";

import {fetchCareerChatHistory} from "../services/app"

function CareerCoach() {

  const { resume_id } = useParams();

  const [chatHistory, setChatHistory] = useState([]);

  useEffect(() => {

    const loadChatHistory = async () => {

      try {

        const data = await fetchCareerChatHistory(resume_id);

        console.log(
          "Career Chat History API Response:",
          data
        );

        setChatHistory(data.history || []);

      } catch (error) {

        console.error(
          "Career Chat History API Error:",
          error
        );

      }

    };

    loadChatHistory();

  }, [resume_id])
}


export default CareerCoach;