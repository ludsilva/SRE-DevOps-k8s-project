const API_URL = "";

async function fetchTasks() {
  const res = await fetch(`${API_URL}/tasks`);
  const data = await res.json();

  const list = document.getElementById("taskList");
  list.innerHTML = "";

  data.forEach(task => {
    const li = document.createElement("li");

    li.className = "flex justify-between items-center bg-gray-700 p-2 rounded";

    li.innerHTML = `
      <span class="${task.done ? 'line-through text-gray-400' : ''}">
        ${task.title}
      </span>
      <button onclick="completeTask(${task.id})"
        class="bg-green-500 px-2 py-1 rounded text-sm hover:bg-green-600">
        ✔
      </button>
    `;

    list.appendChild(li);
  });
}

async function createTask() {
  const input = document.getElementById("taskInput");
  const title = input.value;

  if (!title) return;

  await fetch(`${API_URL}/tasks`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ title })
  });

  input.value = "";
  fetchTasks();
}

async function completeTask(id) {
  await fetch(`${API_URL}/tasks/${id}`, {
    method: "PUT"
  });

  fetchTasks();
}

// inicializa
fetchTasks();