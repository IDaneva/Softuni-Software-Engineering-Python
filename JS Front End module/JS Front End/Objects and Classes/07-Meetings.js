function meetingManager(weeksDayArray) {
    let scheduledDays = {};
    for (line of weeksDayArray) {
        let [day, name] = line.split(' ');
        if (!Object.keys(scheduledDays).includes(day)) {
            scheduledDays[day] = name;
            console.log(`Scheduled for ${day}`);
            
        } else {
            console.log(`Conflict on ${day}!`);
        }
    }

    for (info in scheduledDays) {
        console.log(`${info} -> ${scheduledDays[info]}`);
    }
}

meetingManager(['Friday Bob',

'Saturday Ted',

'Monday Bill',

'Monday John',

'Wednesday George'])