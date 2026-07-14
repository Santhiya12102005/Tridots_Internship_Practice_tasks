let editIndex = -1;
let tasks = JSON.parse(localStorage.getItem("tasks")) || [];
function add()
{
    let taskname = document.getElementById("taskname").value
    let duration = document.getElementById("duration").value
    let status = document.getElementById("status").value
    if (taskname === "" || duration === "" || status==="") {
        alert("Please fill all fields")
        return
    }
    let task={taskname: taskname,duration:duration,status:status}
    tasks.push(task)
    localStorage.setItem("tasks",JSON.stringify(tasks))
    displayTask()
    document.getElementById("taskname").value = ""
    document.getElementById("duration").value = ""
    document.getElementById("status").value = ""

}

function displayTask()
{
    let container=document.getElementById("tasks")
    container.innerHTML=""
    tasks.forEach((task,index)=>{
        container.innerHTML += `
    <tr>
        <td class="text-nowrap">${task.taskname}</td>
        <td class="text-nowrap">${task.duration}</td>
        <td class="text-nowrap">${task.status}</td>
        <td>
            <button class="btn btn-warning btn-sm px-2 py-1" onclick="updateTask(${index})">Update</button>
            <button class="btn btn-danger btn-sm px-2 py-1" onclick="deleteTask(${index})">Delete</button>
        </td>
    </tr>
    `
    })
}

function deleteTask(index){
    if(confirm("Do you want to delete?")){
        tasks.splice(index,1)
        localStorage.setItem("tasks",JSON.stringify(tasks))
    }else{
        displayTask()
    }
    displayTask()
}

function updateTask(index){
    editIndex = index;
    document.getElementById("updateTaskName").value =
    tasks[index].taskname
    document.getElementById("updateDuration").value =
    tasks[index].duration
    document.getElementById("updateStatus").value =
    tasks[index].status
    let modal = new bootstrap.Modal(
        document.getElementById("updateModal")
    )
    modal.show()
}

function saveUpdate(){
    tasks[editIndex].taskname =
    document.getElementById("updateTaskName").value
    tasks[editIndex].duration =
    document.getElementById("updateDuration").value
    tasks[editIndex].status =
    document.getElementById("updateStatus").value
    localStorage.setItem("tasks", JSON.stringify(tasks))
    displayTask()
    bootstrap.Modal.getInstance(
        document.getElementById("updateModal")
    ).hide()
}

displayTask()