function createDeviceCard(icon, ipAddress, mac, lastSeen, scanResults) {

    // Parse last seen timestamp and calculate time difference
    const lastSeenDate = new Date(lastSeen + 'Z');
    const now = new Date();
    const diffSeconds = Math.floor((now - lastSeenDate) / 1000);

    // Calculate value between 0 and 255 based on time difference
    let value = 0;
    if (diffSeconds >= 60) {
        value = 255;
    } else if (diffSeconds > 10) {
        // Linear interpolation between 10 and 60 seconds
        value = Math.floor(((diffSeconds - 10) / (60 - 10)) * 255);
    }

    // Create RGB color value
    const rgbColor = `rgb(${value}, 255, ${value})`;


    // Create the main container div
    const deviceCard = document.createElement('div');
    deviceCard.className = 'row mb-4';

    // Create the inner structure
    const col12 = document.createElement('div');
    col12.className = 'col-12';


    const borderDiv = document.createElement('div');
    borderDiv.className = 'border border-secondary rounded p-4';
    borderDiv.style.backgroundColor = rgbColor;


    const row = document.createElement('div');
    row.className = 'row';

    const col4 = document.createElement('div');
    col4.className = 'col-4 text-center';

    const iconDiv = document.createElement('div');
    iconDiv.className = 'mb-3 big-icon';
    iconDiv.textContent = icon;

    const h5 = document.createElement('h5');
    h5.className = 'text-muted';
    h5.textContent = ipAddress;

    const h5mac = document.createElement('h5');
    h5mac.className = 'text-muted';
    h5mac.textContent = mac;

    const col8 = document.createElement('div');
    col8.className = 'col-8';

    const h6lastSeen = document.createElement('h6');
    h6lastSeen.className = 'text-muted mb-3';
    h6lastSeen.textContent = 'Last Seen: ' + lastSeen + " (" + diffSeconds + "s ago)";

    const h6 = document.createElement('h6');
    h6.className = 'text-muted mb-3';
    h6.textContent = 'Network Scan Results:';

    const bgLightDiv = document.createElement('div');
    bgLightDiv.className = 'bg-light p-3 rounded';

    const code = document.createElement('code');
    code.textContent = scanResults;

    // Assemble the DOM structure
    bgLightDiv.appendChild(code);
    col8.appendChild(h6lastSeen);
    col8.appendChild(h6);
    col8.appendChild(bgLightDiv);

    col4.appendChild(iconDiv);
    col4.appendChild(h5);
    col4.appendChild(h5mac);

    row.appendChild(col4);
    row.appendChild(col8);

    borderDiv.appendChild(row);
    col12.appendChild(borderDiv);
    deviceCard.appendChild(col12);
    return deviceCard;
}

function updateDeviceView(devices) {
    // Get the device container
    const deviceContainer = document.getElementById('device-container');

    // Clear existing content
    deviceContainer.innerHTML = '';

    // Create new device cards for each device in the list
    devices.forEach(device => {
        const deviceCard = createDeviceCard(
            "💻",
            device.last_ip,
            device.mac,
            device.last_seen,
            device.last_scan_results || 'No scan results available'
        );
        deviceContainer.appendChild(deviceCard);
    });
}


let lastFetched = null;

function getDevices() {
    fetch('/api/get-devices')
        .then(response => response.json())
        .then(data => {
            // Check if data is the same as last fetched
            if (JSON.stringify(data) === JSON.stringify(lastFetched)) {
                return; // Exit if data hasn't changed
            }

            // Update lastFetched with current data
            lastFetched = data;

            // Call updateDeviceView with the new data
            updateDeviceView(data);
        })
        .catch(error => {
            console.error('Error fetching devices:', error);
        });
}


document.addEventListener('DOMContentLoaded', function() {
    // Initial call to get devices
    getDevices();

    // Set up timer to call getDevices every 5 seconds
    setInterval(function() {
        getDevices();
    }, 5000);
});

