import React from "react";
import NavBar from "../components/layout/NavBar";
import {Footer} from "../components/layout/Footer";
import {AttemptSurvey} from "../components/surveys/AttemptSurvey";


export default function AttemptSurveyPage() {
    return (
        <>
        <NavBar />
            <AttemptSurvey />
            <Footer />
        </>
    )
}