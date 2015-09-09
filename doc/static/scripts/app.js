/**
* Tox Wiki javascript app.
* @author SkyzohKey, contributors and publishers
* @license WTFPLv2
*/

$(document).ready(function(){
  $(".tooltip-sha1").tooltip({
      title : $(this).data("sha1"),
      placement : 'top'
  });
});

/*function App () {
  this.bindList = [
    {
      'name': 'Tooltips',
      'func': 'this._bindTooltips'
    }
  ];

  this.bindAll = function () {
    for (var i = 0; i < this.bindList.length; i++) {
      var func = eval(this.bindList[i].func + '();');
      console.info('Tox Wiki: binded %s', this.bindList[i].name);
    }
    return true;
  };

  this._bindTooltips = function () {
    console.info('Tooltip applied.');
    $('#last_commit_sha').tooltip();
  };

  this.bindAll();
};


document.onreadystatechange = function () {
    if (document.readyState == "complete") {
        var app = new App();
        $('#last_commit_sha').tooltip();
    }
}*/
