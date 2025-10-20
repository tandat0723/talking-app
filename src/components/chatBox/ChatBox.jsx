import assets from '../../assets/assets'
import './ChatBox.css'

const ChatBox = () => {
  return (
    <div className='chat-box'>
      <div className="chat-user">
        <img src={assets.profile_img} alt="" />
        <p>
          Long
          <img src={assets.green_dot} alt="" className='dot' />
        </p>
        <img src={assets.help_icon} alt="" className='help' />
      </div>
      <div className="chat-msg">
        <div className="s-msg">
          <p className='msg'>Long dang soan tin nhan...</p>
          <div>
            <img src={assets.profile_img} alt='' />
            <p>2:00PM</p>
          </div>
        </div>
        <div className="s-msg">
          <img className='msg-img' src={assets.pic1} alt='' />
          <div>
            <img src={assets.profile_img} alt='' />
            <p>2:00PM</p>
          </div>
        </div>
        <div className="r-msg">
          <p className='msg'>Long dang soan tin nhan...</p>
          <div>
            <img src={assets.profile_img} alt='' />
            <p>2:00PM</p>
          </div>
        </div>
      </div>

      <div className='chat-input'>
        <input type="text" placeholder='Send a message' />
        <input type="file" id='image' accept='image/png, image/jpeg' hidden />
        <lable htmlFor='image'>
          <img src={assets.gallery_icon} alt="" />
        </lable>
        <img src={assets.send_button} alt="" />
      </div>
    </div>
  )
}

export default ChatBox