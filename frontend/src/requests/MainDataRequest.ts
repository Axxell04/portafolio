import { get } from "svelte/store";
import { mainData, URLServer } from "../stores/store";

export async function getMainData() {
  const res = await fetch(`${get(URLServer)}/api/get/main_content`);
  const resBody = await res.json();
  if (res.status === 200) {
    mainData.set(resBody.data)
  }
}
