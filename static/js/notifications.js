
        // Get the notifications
    var notifications = document.getElementsByClassName('notification');
    var start = 3;

    // Initially display the first 3 notifications
    displayNotifications(0, start);

    // On click on "Load more", display the next 3 notifications
    document.getElementById("load-more").addEventListener("click", function(event) {
        event.stopPropagation();
        displayNotifications(start, start + 3);
        start += 3;

        // If all notifications are displayed, hide the button
        if(start >= notifications.length) {
            this.style.display = 'none';
        }
    });

    // When the dropdown is closed, reset the display and the value of start
    document.getElementById('alertsDropdownParent').addEventListener('hide.bs.dropdown', function () {
        start = 3;

        // Hide all notifications
        for(let i = 3; i < notifications.length; i++) {
            notifications[i].style.display = 'none';
        }

        // Show the first 3 notifications
        displayNotifications(0, start);

        // Show the load more button
        document.getElementById("load-more").style.display = 'block';
    });

    // Function to display a range of notifications
    function displayNotifications(start, end) {
        for(let i = start; i < end && i < notifications.length; i++) {
            notifications[i].style.display = 'flex';
        }
    }

