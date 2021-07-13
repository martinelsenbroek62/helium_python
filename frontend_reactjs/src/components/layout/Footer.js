import React from 'react';
import FooterLogo from '../../assets/images/footer.png';

export const Footer = () => {
    return (
        <footer className="text-center mt-5 py-5 footer">
            <div className="my-5 py-5">
                <div className="text-center mb-5">
                    <img src={FooterLogo} width="300" alt="footer Logo" />
                </div>
                <div>
                    <p className="content">Have Questions? E-mail our <span className="BoldUnderline">Support Team</span> for assistance</p>
                    <p className="copyright">© 2017-2019 Sustainability Benefits Corporation</p>
                </div>
            </div>
        </footer>
    );
}