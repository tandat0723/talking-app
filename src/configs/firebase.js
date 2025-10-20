import { createUserWithEmailAndPassword, getAuth, signInWithEmailAndPassword } from "firebase/auth";
import { initializeApp } from "firebase/app";
import { doc, getFirestore, setDoc } from "firebase/firestore";
import { toast } from "react-toastify";

const firebaseConfig = {
  apiKey: "AIzaSyAFZS3fTcgFpGBAthXdNpV3ugWJy7Ic2WQ",
  authDomain: "chat-app-2fbb9.firebaseapp.com",
  projectId: "chat-app-2fbb9",
  storageBucket: "chat-app-2fbb9.firebasestorage.app",
  messagingSenderId: "999888424493",
  appId: "1:999888424493:web:685e8501ae9ce41ae7b2a4"
};

const app = initializeApp(firebaseConfig)
const auth = getAuth(app)
const db = getFirestore(app)

const signup = async (username, email, password) => {
  try {
    const res = await createUserWithEmailAndPassword(auth, email, password)
    const user = res.user
    await setDoc(doc(db, 'users', user.uid), {
      id: user.uid,
      username: username.toLowerCase(),
      email,
      name: "",
      avatar: "",
      bio: "Hey there i am using chat app",
      lastSeen: Date.now()
    })
    await setDoc(doc(db, 'chats', user.uid), {
      chatData: []
    })
  } catch (err) {
    console.error(err)
    toast.error(err.code)
  }
}

const login = async (email, password) => {
  try {
    await signInWithEmailAndPassword(auth, email, password)
  } catch (err) {
    console.error(err)
    toast.error(err.code)
  }
}

export { signup, login }