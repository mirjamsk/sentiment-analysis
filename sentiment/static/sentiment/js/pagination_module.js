/*
 <li class="waves-effect" data-page="2"><a href="#!">2</a></li>
 <li>...</li>
 <li class="waves-effect" data-page="last"><a href="#!">3</a></li>

 */

 /* 

	Pagination Module expects paginationAPI to have these functions defined:
		- getCurrentPage()
		- getNumberOfPages()
		- requestFirstPage()
		- requestLastPage()
		- requestNextPage()	
		- requestPreviousPage();

 */
var PaginationModule = (function(paginationAPI){
	var paginationAPI = paginationAPI;
	var data = {
		firstPage:    1,
		lastPage:     1,
	};

	var util = {
		$paginationComponent : $('<li class="waves-effect" data-page="2"><a href="#!">2</a></li>'),
		$paginationEllipsis  : $('<li>...</li>' ),	
		$paginationContainer : $('ul.pagination'),
		$paginationPrevChevron : $('#prev-page-chevron'),
		$paginationNextChevron : $('#next-page-chevron'),

		disablePaginationChevron: function($paginationChevron){
			$paginationChevron.addClass('disabled');
			$paginationChevron.removeClass('waves-effect');
		},		
		enablePaginationChevron: function($paginationChevron){
			$paginationChevron.removeClass('disabled' );
			$paginationChevron.addClass('waves-effect');
		},
		createPaginationComponent: function(pageNumber){
			var $paginationComponent = this.$paginationComponent.clone();
			$paginationComponent.attr('data-page', pageNumber);
			$paginationComponent.find('a').text(pageNumber);
			return $paginationComponent;
		},
		insertPaginationComponent: function(pageNumber){
			if (isNaN(pageNumber) || pageNumber == data.firstPage) return;
			var $prevPageComponent = this.$paginationContainer.find('[data-page="'+ (pageNumber-1) +'"]')[0];
			var $paginationComponent = this.createPaginationComponent(pageNumber);
			$paginationComponent.insertAfter($prevPageComponent);
		},
		insertPaginationEllipsis: function(prevPageNumber){
			if (isNaN(prevPageNumber) || prevPageNumber == data.firstPage) return;
			var $prevPageComponent = this.$paginationContainer.find('[data-page="'+ prevPageNumber +'"]')[0];
			var $ellipsisComponent = this.$paginationEllipsis.clone();
			$ellipsisComponent.insertAfter($prevPageComponent);
		}
	};

	var handleClickEvent = function(){
		var pageData = $(this).data('page');
		if(pageData === 'prev')
			paginationAPI.requestPreviousPage();
		else if(pageData === 'next'){
			paginationAPI.requestNextPage();
		}
		else if(pageData === data.lastPage){
			paginationAPI.requestLastPage();
		}
		else if(pageData === data.firstPage){
			paginationAPI.requestFirstPage();
		}



	};
	var bindClickEvent = function(){
		util.$paginationContainer.on('click', 'li', handleClickEvent);

	};


	// initial setup
	(function(){
		console.log('paginationSetup');
		data.lastPage = paginationAPI.getNumberOfPages();

		if (isNaN(data.lastPage) || data.lastPage <= 1) return;
		if (data.lastPage > 2){
			util.insertPaginationComponent(2);
		}
		if (data.lastPage > 3){
			util.insertPaginationComponent(3);
		}
		if (data.lastPage > 4){
			util.insertPaginationEllipsis(Math.min(data.lastPage,3));
		}
		
		var $lastPage = util.createPaginationComponent(data.lastPage);
		$lastPage.insertBefore(util.$paginationNextChevron);
		util.enablePaginationChevron(util.$paginationNextChevron);
		bindClickEvent()

	})();

});
