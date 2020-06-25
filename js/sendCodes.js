$(document).ready(function(){

var remote_end = "http://yellowpages.rw/projects/benax/run/catch-ajax.php";
var device = "Benax-3.0-1";

$.get("http://ipinfo.io", function(response) {
   ip = response.ip;      //Declare without var puts it in the GLOBAL Category  
}, "jsonp");



/*************** SEND CODES *****************************************************/		

		$('#benax-terminal-textarea').bind('copy', function() {
		    $.ajax({
			url:"createStopScript.php",
			beforeSend: function(){},
			success:function(data){}
		    });
		});	
		
		
		$('#benax-terminal-run-button').on('click', function(event){
			
			event.preventDefault();
			
			var codes = $('#benax-terminal-textarea').val();
			

			if(codes == ''){
				
				$('#last_codes').html(codes+"<br><span style='font-size: 14px; margin-left: 10px; '>Last scripts, "+new Date().toLocaleString()+"</span>");
										
		
			}
			
			else if(codes.includes('kubitsa:')){

				$.ajax({
					url:"commandSaver.php",
					method:"POST",
					data:{'command':codes},
					beforeSend: function(){
						/*
						Do something here!
						*/
						},
					success:function(data)
					{
			
						$('#codes_form')[0].reset();
						$('#benax-terminal-run-button').show();
						$('#benax-terminal-textarea').focus();
						$('#benax-terminal-textarea').html("");
						$('#last_codes').html(codes+"<br><br><span style='font-size: 14px; margin-left: 10px; '>Last scripts, "+new Date().toLocaleString()+"</span>");
						
		
					}
				});

			    	$.ajax({
					url:remote_end,
					method:"POST",
					data:{'command':codes,'device':device,'ip':ip},
					beforeSend: function(){},
					success:function(data){}
		    	    	});
				
			}

			else if(codes.includes('kubikuza:')){

				$.ajax({
					url:"commandRetriever.php",
					method:"POST",
					data:{'command':codes},
					beforeSend: function(){
						/*
						Do something here!
						*/
						},
					success:function(data)
					{
			
						$('#codes_form')[0].reset();
						$('#benax-terminal-run-button').show();
						$('#benax-terminal-textarea').html(data);
						$('#last_codes').html(codes+"<br><br><span style='font-size: 14px; margin-left: 10px; '>Last scripts, "+new Date().toLocaleString()+"</span>");
								
		
					}
				});

			    	$.ajax({
					url:remote_end,
					method:"POST",
					data:{'command':codes,'device':device,'ip':ip},
					beforeSend: function(){},
					success:function(data){}
		    	    	});
				
			}


			else if(codes.includes('gusiba:')){

				$.ajax({
					url:"commandRemover.php",
					method:"POST",
					data:{'command':codes},
					beforeSend: function(){
						/*
						Do something here!
						*/
						},
					success:function(data)
					{
			
						$('#codes_form')[0].reset();
						$('#benax-terminal-run-button').show();
						$('#benax-terminal-textarea').html(data);
						$('#last_codes').html(codes+"<br><br><span style='font-size: 14px; margin-left: 10px; '>Last scripts, "+new Date().toLocaleString()+"</span>");
						
		
					}
				});

			    	$.ajax({
					url:remote_end,
					method:"POST",
					data:{'command':codes,'device':device,'ip':ip},
					beforeSend: function(){},
					success:function(data){}
		    	    	});
				
			}


			else if(codes.includes('ububiko')){

				$.ajax({
					url:"savedFilesChecker.php",
					method:"POST",
					data:{'command':codes},
					beforeSend: function(){
						/*
						Do something here!
						*/
						},
					success:function(data)
					{
			
						$('#codes_form')[0].reset();
						$('#benax-terminal-run-button').show();
						$('#benax-terminal-textarea').html(data);
						//$('#benax-terminal-textarea').attr('readonly','readonly');
						$('#last_codes').html(codes+"<br><br><span style='font-size: 14px; margin-left: 10px; '>Last scripts, "+new Date().toLocaleString()+"</span>");
						
		
					}
				});

			    	$.ajax({
					url:remote_end,
					method:"POST",
					data:{'command':codes,'device':device,'ip':ip},
					beforeSend: function(){},
					success:function(data){}
		    	    	});
				
			}
			
						else if(codes.includes('gukoresha:')){

				$.ajax({
					url:"commandRunner.php",
					method:"POST",
					data:{'command':codes},
					beforeSend: function(){
						/*
						Do something here!
						*/
						},
					success:function(data)
					{
			
						$('#codes_form')[0].reset();
						$('#benax-terminal-run-button').show();
						$('#benax-terminal-textarea').focus();
						$('#benax-terminal-textarea').html("");
						$('#last_codes').html(codes+"<br><br><span style='font-size: 14px; margin-left: 10px; '>Last scripts, "+new Date().toLocaleString()+"</span>");
						
		
					}
				});

			    	$.ajax({
					url:remote_end,
					method:"POST",
					data:{'command':codes,'device':device,'ip':ip},
					beforeSend: function(){},
					success:function(data){}
		    	    	});
				
			}
			
			else if(codes == '?'){
				
				$('#codes_form')[0].reset();
				$('#benax-terminal-textarea').html("#01: imbere(how long in seconds): go straight forward.\n\n"+
				"#02: inyuma(how long in seconds): go straight backward\n\n"+
				"#03: iburyo(how long in seconds): turn right\n\n"+
				"#04: ibumoso(how long in seconds): turn left\n\n"+		
				"#05: ruhuka(how long in seconds): turn left\n\n"+	
				"#06: bisubiremo(how many times): turn left\n\n"+	
				"#07: ikaramuhasi: pencil ready to write\n\n"+
				"#11: fotora: take picture\n\n");
				
			}
			
			else if (codes.includes('fotora')){
				
				$('#loadPic').show();
				$('#loadPicHeader').show();	
				$('#closeButton').show();				

				
				$.ajax({
					url:"interpreter.php",
					method:"POST",
					data:{'command':codes},
					beforeSend: function(){
						$('#load_pic').html('Loading...');
					},
					success:function(data)
					{
			
						$('#codes_form')[0].reset();
						$('#benax-terminal-run-button').show();
						$('#benax-terminal-textarea').focus();
						$('#last_codes').html(codes+"<br><br><span style='font-size: 14px; margin-left: 10px; '>Last scripts, "+new Date().toLocaleString()+"</span>");
						$('#load_pic').load('loadPic.php').fadeIn("fast");
						
			
			
		
					}
				});

			    	$.ajax({
					url:remote_end,
					method:"POST",
					data:{'command':codes,'device':device,'ip':ip},
					beforeSend: function(){},
					success:function(data){}
		    	    	});
				
			}
				
	
			
			
			else{
				$.ajax({
					url:"interpreter.php",
					method:"POST",
					data:{'command':codes},
					beforeSend: function(){
						$('#benax-terminal-textarea').focus();
						},
					success:function(data)
					{
			
						$('#codes_form')[0].reset();
						$('#benax-terminal-run-button').show();
						$('#benax-terminal-textarea').html(data);
						$('#benax-terminal-textarea').focus();
						$('#last_codes').html(codes+"<br><br><span style='font-size: 14px; margin-left: 10px; '>Last scripts, "+new Date().toLocaleString()+"</span>");
						
		
					}
				});

			    	$.ajax({
					url:remote_end,
					method:"POST",
					data:{'command':codes,'device':device,'ip':ip},
					beforeSend: function(){},
					success:function(data){}
		    	    	});


			}
		
		});
		







dragElement(document.getElementById(("loadPic")));

function dragElement(elmnt) {
  var pos1 = 0, pos2 = 0, pos3 = 0, pos4 = 0;
  if (document.getElementById(elmnt.id + "Header")) {
    /* if present, the header is where you move the DIV from:*/
    document.getElementById(elmnt.id + "Header").onmousedown = dragMouseDown;
  } else {
    /* otherwise, move the DIV from anywhere inside the DIV:*/
    elmnt.onmousedown = dragMouseDown;
  }

  function dragMouseDown(e) {
    e = e || window.event;
    // get the mouse cursor position at startup:
    pos3 = e.clientX;
    pos4 = e.clientY;
    document.onmouseup = closeDragElement;
    // call a function whenever the cursor moves:
    document.onmousemove = elementDrag;
  }

  function elementDrag(e) {
    e = e || window.event;
    // calculate the new cursor position:
    pos1 = pos3 - e.clientX;
    pos2 = pos4 - e.clientY;
    pos3 = e.clientX;
    pos4 = e.clientY;
    // set the element's new position:
    elmnt.style.top = (elmnt.offsetTop - pos2) + "px";
    elmnt.style.left = (elmnt.offsetLeft - pos1) + "px";
  }

  function closeDragElement() {
    /* stop moving when mouse button is released:*/
    document.onmouseup = null;
    document.onmousemove = null;
  }
}




	
		
});


function hideAllThis(){
	$('#load_pic').html('');
	$('#loadPicHeader').hide();
	location.reload();
	
}



