<script lang="ts">
  import { slide } from "svelte/transition";
  import { isLogged, loginVisible, URLServer, usernameSession } from "../../../stores/store";
  import { get } from "svelte/store";

  async function logout () {
    const res = await fetch(`${get(URLServer)}/logout`)
    if (res.status === 200) {
        isLogged.set(false);
        usernameSession.set("");
        loginVisible.set(false);
        
    }
  }

</script>

<div class="flex justify-center">
  <button
    transition:slide
    class="border rounded px-2 w-fit hover:bg-neutral-800 hover:cursor-pointer text-neutral-400 hover:text-neutral-300"
   on:click={logout}>
    Logout
  </button>
</div>
