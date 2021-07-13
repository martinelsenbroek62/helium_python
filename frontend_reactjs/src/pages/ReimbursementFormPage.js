import React from "react";
import NavBar from "../components/layout/NavBar";
import {Footer} from "../components/layout/Footer";
import ReimbursementForm from "../components/claims/ReimbursementForm";


export default function ReimbursementFormPage() {
    return (
        <>
            <NavBar/>
            <ReimbursementForm/>
            <Footer/>
        </>
    )
}