import React from "react";
import NavBar from "../components/layout/NavBar"
import {Footer} from "../components/layout/Footer";
import {Profile} from "../components/users/Profile";

export default function ProfilePage() {
  return (
    <>
        <NavBar />
        <Profile />
        <Footer />
    </>
  );
}
