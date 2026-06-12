import React, { useReducer, useState } from 'react'
import "./App.css"

const App = () => {

  const [UserMessage, setUserMessage] = useState("")
  const [RecivedMessage, setRecivedMessage] = useState([])
  const [Chat, setChat] = useState([])

  const DataFetching = async() =>{

    const response = await fetch("http://127.0.0.1:8000/chat",
      {
        method: "POST",
        headers:{
          "Content-Type":"application/json"
        },
        body: JSON.stringify({message: UserMessage})
      }
    )
      const RecivedMessage = await response.json()
    console.log(RecivedMessage);
  }
  return (
    <div >
      <div><h2>Enter /file to attach file</h2></div>
      <input type="text"
      value={UserMessage}
      onChange={(e)=>{
            setUserMessage(e.target.value)
        console.log(UserMessage);
      }}
      />
      <button onClick={()=>{
        if(!UserMessage)
          return

        DataFetching()
        setChat((prevChat ) =>[...Chat, UserMessage])
        setUserMessage("")
        console.log(Chat);
      }}>Send</button>
      <div>
        {
          Chat && Chat.length > 0 ? (

            <h2>{Chat.map((RecivedMessage,index,Chat)=>{
              return(
                <div key={index}>
                  <h5 className='UserChatBox'>User chat:{Chat[index]}
                    </h5>
                    <h5>Reply chat:{RecivedMessage}</h5>
                </div>
              )
            })}</h2>
          ): 
          <h2>Start the conversation </h2>
        }
          </div>
    </div>
  )
}

export default App