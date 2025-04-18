console.log("App Start");
let completeData, season01, season02, season03, season04, season05, season06, season07, season08, season09, season10;

Promise.all([
    d3.csv('data/complete.csv'),
    d3.csv('data/season01.csv'),
    d3.csv('data/season02.csv'),
    d3.csv('data/season03.csv'),
    d3.csv('data/season04.csv'),
    d3.csv('data/season05.csv'),
    d3.csv('data/season06.csv'),
    d3.csv('data/season07.csv'),
    d3.csv('data/season08.csv'),
    d3.csv('data/season09.csv'),
    d3.csv('data/season10.csv')
  ]).then(_data => {
    console.log('Data loading complete. Work with dataset.');
    completeData = _data[0];
    season01 = _data[1];
    season02 = _data[2];
    season03 = _data[3];
    season04 = _data[4];
    season05 = _data[5];
    season06 = _data[6];
    season07 = _data[7];
    season08 = _data[8];
    season09 = _data[9];
    season10 = _data[10];

    // Rest is TODO
  })
  .catch(error => {
    console.error('Error: Failed to load data!');
    console.log(error);
  });