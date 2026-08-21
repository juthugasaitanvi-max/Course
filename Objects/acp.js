let favouritePerson = {
      name:         "Sai Tanish",
      relationship: "My Big Brother",
      activity:     "Coding",
      city:         "Hyderabad"
    };

    let nameEl = document.getElementById("name");
    let relationshipEl = document.getElementById("relationship");
    nameEl.textContent = favouritePerson.name;
    relationshipEl.textContent = favouritePerson.relationship;

   
    let activityEl = document.getElementById("activity");
    let cityEl = document.getElementById("city");
    activityEl.textContent = favouritePerson["activity"];
    cityEl.textContent = favouritePerson["city"];

    
    let codeEl = document.getElementById("codeDisplay");
    codeEl.textContent =
      'let favouritePerson = {\n' +
      '  name:         "' + favouritePerson.name + '",\n' +
      '  relationship: "' + favouritePerson.relationship + '",\n' +
      '  activity:     "' + favouritePerson["activity"] + '",\n' +
      '  city:         "' + favouritePerson["city"] + '"\n' +
      '};';
    
    