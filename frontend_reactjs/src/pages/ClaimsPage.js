import React from "react";
import NavBar from "../components/layout/NavBar";
import {Footer} from "../components/layout/Footer";
import Claims from "../components/claims/Claims";


export default function ClaimsPage() {
    return (
        <>
        <NavBar />
            <Claims />
            <Footer />
        </>
    )
}