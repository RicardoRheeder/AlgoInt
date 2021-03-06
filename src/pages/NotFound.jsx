import React, { Component } from 'react'

/** This was used for 404 errors */
export default class UnderDev extends Component {
    render() {
        return (
            <div className="notfound-root">
                <div className="page-text">
                    <b>404</b>{`. That's an error.\n\n`}
                    {`The requested URL was not found on this server.\nThat's all we know.`}
                </div>
                <div className="image-container">
                    <img src='assets/greenfoot404.gif'/>
                </div>
            </div>
        )
    }
}