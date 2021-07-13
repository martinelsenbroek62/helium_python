import React from "react";
import NavBar from "../components/layout/NavBar"
import Home from "../components/general/Home"
import {Footer} from "../components/layout/Footer";

export default function HomePage() {
  return (
    <>
        <NavBar />
        <Home />
        <Footer />
    </>
  );
}
