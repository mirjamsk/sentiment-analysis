// Sample usage:
// $('#elem').materializePagination({ message: 'Goodbye World!'});

(function($, window, document, undefined) {

    // our materializePagination constructor
    var MaterializePagination = function(elem, options) {
        this.elem = elem;
        this.$elem = $(elem);
        this.options = options;
        this.$container = null;
        this.$firstPage = null;
        this.$lastPage = null;
        this.$prevChevron = null;
        this.$nextChevron = null;
        this.$prevEllipsis = null;
        this.$nextEllipsis = null;
        this.currentPage = 1;
        this.visiblePages = [];
        this.maxVisiblePages = 3;
    };

    // the materializePagination prototype
    MaterializePagination.prototype = {
        defaults: {
            align: 'center',
            lastPage: 1,
            firstPage: 1,
            currentPage: 1,
            urlParameter: 'page',
            changeUrlParams: true,
            onClickCallback: null
        },

        init: function() {
            this.config = $.extend({}, this.defaults, this.options);
            var requestedPage = this.getParameterByName(this.config.urlParameter) || 1;
            requestedPage = isNaN(requestedPage) || requestedPage > this.config.lastPage ? 1 : parseInt(requestedPage);
            this.createPaginationBase(requestedPage);
            this.bindClickEvent();
            return this;
        },
        renderActivePage: function() {
            this.config.onClickCallback(this.currentPage);
            this.$container.find('li.active').removeClass('active');
            var currentPageComponent = $(this.$container.find('[data-page="' + this.currentPage + '"]')[0]);
            currentPageComponent.addClass('active');
            window.history.pushState('', '', '?'+ this.config.urlParameter +'=' + this.currentPage);
        },
        requestPrevPage: function() {
            this.currentPage -= 1;

            if (this.currentPage === this.config.lastPage - this.maxVisiblePages)
                this.$nextEllipsis.removeClass('hide');

            if (this.currentPage === this.config.firstPage + this.maxVisiblePages - 1)
                this.$prevEllipsis.addClass('hide');

            this.visiblePages.pop().remove();
            this.visiblePages.unshift(this.insertPrevPaginationComponent(this.currentPage - 1));
        },

        requestNextPage: function() {
            this.currentPage += 1;

            if (this.currentPage === this.config.firstPage + this.maxVisiblePages)
                this.$prevEllipsis.removeClass('hide');

            if (this.currentPage === this.config.lastPage - this.maxVisiblePages + 1)
                this.$nextEllipsis.addClass('hide');

            this.visiblePages.shift().remove();
            this.visiblePages.push(this.insertNextPaginationComponent(this.currentPage + 1));
        },

        requestFirstPage: function() {
            this.currentPage = 1;
            this.purgeVisiblePages();
            this.$firstPage.addClass('active');

            for (var page = 1; page < this.maxVisiblePages; page += 1) {
                this.visiblePages.push($(''));
            }
            //for (var page = 2; page < Math.min(this.config.lastPage, this.maxVisiblePages); page += 1) 
            var $paginationComoponent = this.insertNextPaginationComponent(this.maxVisiblePages - 1);
            this.visiblePages.push($paginationComoponent);

            if (this.config.lastPage > this.maxVisiblePages) {
                this.$nextEllipsis.removeClass('hide');
                this.$prevEllipsis.addClass('hide');
            }
        },

        requestLastPage: function() {
            this.currentPage = this.config.lastPage;
            this.purgeVisiblePages();
            this.$firstPage.addClass('active');

            for (var page = 1; page < this.maxVisiblePages; page += 1) {
                this.visiblePages.push($(''));
            }

            //for (var page = 2; page < Math.min(this.config.lastPage, this.maxVisiblePages); page += 1) 
            var $paginationComoponent = this.insertNextPaginationComponent(this.config.lastPage - 1);
            this.visiblePages.unshift($paginationComoponent);

            if (this.config.lastPage > this.maxVisiblePages) {
                this.$nextEllipsis.addClass('hide');
                this.$prevEllipsis.removeClass('hide');
            }
        },

        requestPage: function(page) {
            this.currentPage = page;
            this.purgeVisiblePages();
            this.visiblePages.push(this.insertPrevPaginationComponent(this.currentPage - 1));
            this.visiblePages.push(this.insertNextPaginationComponent(this.currentPage));
            this.visiblePages.push(this.insertNextPaginationComponent(this.currentPage + 1));
            this.renderActivePage();
            if (this.currentPage >= this.config.firstPage + this.maxVisiblePages)
                this.$prevEllipsis.removeClass('hide');
            if (this.currentPage <= this.config.lastPage - this.maxVisiblePages)
                this.$nextEllipsis.removeClass('hide');
        },

        purgeVisiblePages: function() {
            var size = this.visiblePages.length;
            for (var page = 0; page < size; page += 1) {
                this.visiblePages.pop().remove();
            }
        },

        bindClickEvent: function() {
            var self = this;
            this.$container.on('click', 'li', function() {
                var pageData = $(this).data('page');
                if (pageData === self.currentPage) {
                    return;
                } else if ((pageData === 'prev' || pageData == self.currentPage - 1) && self.currentPage !== self.config.firstPage) {
                    self.requestPrevPage();
                } else if ((pageData === 'next' || pageData == self.currentPage + 1) && self.currentPage !== self.config.lastPage) {
                    self.requestNextPage();
                } else if (!isNaN(pageData) && pageData == self.config.firstPage) {
                    self.requestFirstPage();
                } else if (!isNaN(pageData) && pageData == self.config.lastPage) {
                    self.requestLastPage();
                }
                self.renderActivePage();
            });

        },

        createPaginationBase: function(requestedPage) {
            if (isNaN(this.config.lastPage) || this.config.lastPage < 1) return;

            this.$container = $('<ul>');
            this.$container.addClass('pagination');
            this.$container.addClass(this.config.align + '-align');

            this.$firstPage = this.createPaginationComponent(this.config.firstPage);
            this.$prevChevron = this.createPaginationChevron('prev');
            this.$nextChevron = this.createPaginationChevron('next');
            this.$prevEllipsis = this.createPaginationEllipsis();
            this.$nextEllipsis = this.createPaginationEllipsis();

            this.$container.append(this.$prevChevron);
            this.$container.append(this.$firstPage);
            this.$container.append(this.$prevEllipsis);
            this.$container.append(this.$nextEllipsis);
            this.$container.append(this.$nextChevron);

            if (this.config.lastPage > this.config.firstPage) {
                this.$lastPage = this.createPaginationComponent(this.config.lastPage);
                this.$lastPage.insertBefore(this.$nextChevron);
            }

            switch (requestedPage) {
                case this.config.firstPage:
                    this.requestFirstPage();
                    break;
                case this.config.lastPage:
                    this.requestLastPage();
                    break;
                default:
                    this.requestPage(requestedPage);
                    break;
            }

            this.$elem.append(this.$container);
        },

        util: {
            $paginationComponent: $('<li class="waves-effect" data-page="1"><a href="#!">1</a></li>'),
            $paginationEllipsis: $('<li class="hide">...</li>'),
        },

        createPaginationComponent: function(pageNumber) {
            var $paginationComponent = this.util.$paginationComponent.clone();
            $paginationComponent.attr('data-page', pageNumber);
            $paginationComponent.find('a').text(pageNumber);
            return $paginationComponent;
        },

        insertPrevPaginationComponent: function(pageNumber) {
            if (isNaN(pageNumber) || pageNumber <= this.config.firstPage) return $('');
            var $paginationComponent = this.createPaginationComponent(pageNumber);
            $paginationComponent.insertAfter(this.$prevEllipsis);
            return $paginationComponent;
        },

        insertNextPaginationComponent: function(pageNumber) {
            if (isNaN(pageNumber) || pageNumber >= this.config.lastPage) return $('');
            var $paginationComponent = this.createPaginationComponent(pageNumber);
            $paginationComponent.insertBefore(this.$nextEllipsis);
            return $paginationComponent;
        },

        createPaginationChevron: function(type) {
            var direction = type === 'next' ? 'right' : 'left';
            return $(
                '<li data-page="' + type + '">\
				        <a href="#!"><i class="material-icons">chevron_' + direction + '</i></a>\
			    </li>'
            );
        },

        createPaginationEllipsis: function() {
            return this.util.$paginationEllipsis.clone();
        },

        getParameterByName: function(name) {
            url = window.location.href;
            name = name.replace(/[\[\]]/g, "\\$&");
            var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)"),
                results = regex.exec(url);
            if (!results) return null;
            if (!results[2]) return '';
            return decodeURIComponent(results[2].replace(/\+/g, " "));
        }

    };

    MaterializePagination.defaults = MaterializePagination.prototype.defaults;

    $.fn.materializePagination = function(options) {
        return this.each(function() {
            new MaterializePagination(this, options).init();
        });
    };

})(jQuery, window, document);
