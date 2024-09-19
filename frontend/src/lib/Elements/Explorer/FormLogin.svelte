<script lang="ts">
  import { fade, slide } from "svelte/transition";
  import { isLogged, loginVisible, URLServer, usernameSession } from "../../../stores/store";
  import { get } from "svelte/store";

  let alertUsername = false;
  let alertPassword = false;

  let username: string;
  let password: string;

  function setUsername (e: Event) {
    if (e.target != null && "value" in e.target && typeof e.target.value === "string") {
        username = e.target.value;
        alertUsername = false;
    }
  }
  function setPassword (e: Event) {
    if (e.target != null && "value" in e.target && typeof e.target.value === "string") {
        password = e.target.value;
        alertPassword = false;
    }
  }

  async function logUser () {
    if (!username) {alertUsername = true};
    if (!password) {alertPassword = true}; 
    
    if (alertUsername || alertPassword) {return}
    
    const res = await fetch(`${get(URLServer)}/login`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        credentials: 'include',
        body: JSON.stringify({
            username: username,
            password: password
        })
    });
    if (res.status === 200) {
        console.log(await res.json())
        isLogged.set(true);
        usernameSession.set(username);
        username = "";
        password = "";
        loginVisible.set(false);
    }
  }

</script>

<div transition:fade class=" text-neutral-300">
    <div class="flex flex-col gap-2 place-items-center">
      <div class="flex flex-col">
        <label for="username">Username</label>
        <input type="text" name="username" required class=" bg-transparent border rounded px-1 text-neutral-400 w-40 {alertUsername ? 'border-red-500' : ''}" on:input={e => setUsername(e)}>
      </div>
      <div class="flex flex-col">
        <label for="password">Password</label>
        <input type="password" name="password" required class=" bg-transparent border rounded px-1 text-neutral-400 w-40 {alertPassword ? 'border-red-500': ''}" on:input={e => setPassword(e)}>
      </div>
      <button class="border rounded px-2 w-fit place-self-center hover:bg-neutral-800 hover:cursor-pointer" on:click={logUser}>
        Login
      </button>
    </div>
  </div>