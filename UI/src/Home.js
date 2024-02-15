import { useNavigate } from 'react-router-dom';
import "./Home.css";
import { jsx as _jsx } from "react/jsx-runtime";
import { jsxs as _jsxs } from "react/jsx-runtime";

export const Home = () => {
  const navigate = useNavigate(); // This line was missing

  return /*#__PURE__*/_jsx("div", {
    className: "box",
    children: /*#__PURE__*/_jsx("div", {
      className: "home-page",
      children: /*#__PURE__*/_jsxs("div", {
        className: "group",
        children: [/*#__PURE__*/_jsx("div", {
          className: "group-wrapper",
          children: /*#__PURE__*/_jsx("div", {
            className: "div-wrapper",
            children: /*#__PURE__*/_jsx("p", {
              className: "text-wrapper",
              children: "Download Desktop App for Windows"
            })
          })
        }), /*#__PURE__*/_jsx("div", {
          className: "div",
          children: /*#__PURE__*/_jsxs("div", {
            className: "group-2",
            children: [/*#__PURE__*/_jsx("div", {
              className: "overlap-group-wrapper",
              children: /*#__PURE__*/_jsx("div", {
                className: "overlap-group",
                onClick: () => navigate('/settings'), // Now 'navigate' is defined
                children: /*#__PURE__*/_jsx("div", {
                  className: "text-wrapper-2",
                  children: "Starcraft 2"
                })
              })
            }), /*#__PURE__*/_jsx("div", {
              className: "overlap-wrapper",
              children: /*#__PURE__*/_jsx("div", {
                className: "overlap-group",
                children: /*#__PURE__*/_jsx("div", {
                  className: "text-wrapper-2",
                  children: "ZeroSpace"
                })
              })
            }), /*#__PURE__*/_jsx("div", {
              className: "group-3",
              children: /*#__PURE__*/_jsx("div", {
                className: "overlap-group",
                children: /*#__PURE__*/_jsx("div", {
                  className: "text-wrapper-2",
                  children: "StormGate"
                })
              })
            })]
          })
        })]
      })
    })
  });
};

export default Home;
